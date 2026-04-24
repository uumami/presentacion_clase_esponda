#!/usr/bin/env python3
"""
Genera imágenes para la presentación parseando prompts/nano_banana_prompts.txt
y llamando a Gemini 2.5 Flash Image (Nano Banana) vía google-genai.

Uso:
    export GEMINI_API_KEY=...   # o GOOGLE_API_KEY
    python scripts/generate_images.py
    python scripts/generate_images.py --only 01,02,07         # slides específicos
    python scripts/generate_images.py --skip-existing         # no regenerar
    python scripts/generate_images.py --parallel 3            # N en paralelo
    python scripts/generate_images.py --dry-run               # solo lista

Formato del prompts.txt:
    ## SLIDE XX — título
    File:   img/<path>.png
    ...metadata libre (Ancla:, Nota:, etc)...
    Prompt:
    ---
    <texto multilinea>
    ---

Si hay múltiples File: y múltiples "Prompt NN:" en un bloque, se asocian
por orden. Si hay un solo Prompt: sirve para todos los File: del bloque.
Bloques con [SKIP] o [FOTO REAL] se ignoran.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPTS_PATH = ROOT / "prompts" / "nano_banana_prompts.txt"
OUT_ROOT = ROOT / "deck" / "public"
CACHE_DIR = ROOT / ".cache" / "nano_banana"
MODEL = os.environ.get("NANO_BANANA_MODEL", "gemini-3.1-flash-image-preview")


@dataclass
class ImgJob:
    slide: str
    file_path: Path
    prompt: str
    skip: bool = False
    tags: list[str] = field(default_factory=list)

    @property
    def hash(self) -> str:
        return hashlib.sha256(
            (MODEL + "|" + self.prompt).encode("utf-8")
        ).hexdigest()[:16]


def parse_prompts(text: str) -> list[ImgJob]:
    """Parse the prompts.txt into a list of ImgJob."""
    jobs: list[ImgJob] = []

    # Split into slide blocks by the ## SLIDE header
    blocks = re.split(r"^## SLIDE\s+", text, flags=re.MULTILINE)
    for block in blocks[1:]:
        # First line: "XX — title"
        header_match = re.match(r"(\S+)\s*—\s*(.+)", block)
        if not header_match:
            continue
        slide_num = header_match.group(1).strip()
        skip = "[SKIP]" in block or "[FOTO REAL]" in block

        files = re.findall(r"^File:\s*(\S+)(?:\s+\[([^\]]+)\])?", block, flags=re.MULTILINE)
        if not files:
            continue

        # Extract prompts between --- ... --- markers
        prompt_bodies = re.findall(r"^---\s*$(.*?)^---\s*$", block, flags=re.MULTILINE | re.DOTALL)
        prompt_bodies = [p.strip() for p in prompt_bodies if p.strip()]

        if not prompt_bodies:
            continue

        # Associate files with prompts
        for i, (fpath, tag) in enumerate(files):
            if len(prompt_bodies) == 1:
                prompt_text = prompt_bodies[0]
            elif i < len(prompt_bodies):
                prompt_text = prompt_bodies[i]
            else:
                prompt_text = prompt_bodies[-1]

            file_tag = tag or ""
            file_skip = skip or "SKIP" in file_tag.upper() or "FOTO REAL" in file_tag.upper()

            jobs.append(
                ImgJob(
                    slide=slide_num,
                    file_path=OUT_ROOT / fpath,
                    prompt=prompt_text,
                    skip=file_skip,
                    tags=[file_tag] if file_tag else [],
                )
            )

    return jobs


def load_dotenv(path: Path):
    """Minimal .env loader (no external dep). KEY=VALUE per line, # comments ok."""
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        k = k.strip()
        v = v.strip().strip('"').strip("'")
        if k and k not in os.environ:
            os.environ[k] = v


def load_client():
    load_dotenv(ROOT / ".env")
    try:
        from google import genai  # type: ignore
    except ImportError as e:
        sys.exit(
            "ERROR: google-genai no está instalado.\n"
            "   pip install google-genai\n"
            f"   detalle: {e}"
        )

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        sys.exit(
            "ERROR: no encuentro GEMINI_API_KEY ni GOOGLE_API_KEY en el env ni en .env.\n"
            "   export GEMINI_API_KEY=..."
        )
    return genai.Client(api_key=api_key)


def save_bytes(path: Path, data: bytes):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def cache_path(job: ImgJob) -> Path:
    return CACHE_DIR / f"{job.hash}.png"


def generate_one(client, job: ImgJob, skip_existing: bool) -> tuple[ImgJob, str]:
    """Generate one image. Returns (job, status_str)."""
    if job.skip:
        return job, "SKIP (marked)"

    if skip_existing and job.file_path.exists() and job.file_path.stat().st_size > 1024:
        return job, "SKIP (exists)"

    cache = cache_path(job)
    if cache.exists():
        save_bytes(job.file_path, cache.read_bytes())
        return job, "CACHE hit"

    try:
        resp = client.models.generate_content(
            model=MODEL,
            contents=job.prompt,
        )
    except Exception as e:
        return job, f"FAIL (api): {e}"

    img_bytes = None
    for cand in getattr(resp, "candidates", []) or []:
        for part in getattr(getattr(cand, "content", None), "parts", []) or []:
            inline = getattr(part, "inline_data", None)
            if inline and getattr(inline, "data", None):
                img_bytes = inline.data
                break
        if img_bytes:
            break

    if not img_bytes:
        return job, "FAIL (no image returned)"

    save_bytes(cache, img_bytes)
    save_bytes(job.file_path, img_bytes)
    return job, f"OK ({len(img_bytes)} bytes)"


def main():
    ap = argparse.ArgumentParser(description="Genera imágenes con Nano Banana.")
    ap.add_argument("--only", help="slides a generar: '01,02,07'")
    ap.add_argument("--skip-existing", action="store_true", help="no regenerar si ya existe")
    ap.add_argument("--parallel", type=int, default=1, help="N workers en paralelo (1 default)")
    ap.add_argument("--dry-run", action="store_true", help="solo listar jobs")
    args = ap.parse_args()

    if not PROMPTS_PATH.exists():
        sys.exit(f"ERROR: no encuentro {PROMPTS_PATH}")

    text = PROMPTS_PATH.read_text(encoding="utf-8")
    jobs = parse_prompts(text)
    if not jobs:
        sys.exit("ERROR: no parseé ningún job. revisa el formato de prompts.txt.")

    if args.only:
        keep = set(args.only.split(","))
        jobs = [j for j in jobs if j.slide in keep]

    print(f"[i] {len(jobs)} imágenes · modelo={MODEL}")
    print(f"[i] output root: {OUT_ROOT}")
    for j in jobs:
        status = "SKIP" if j.skip else "GEN"
        rel = j.file_path.relative_to(OUT_ROOT)
        print(f"    [{status}] slide {j.slide:>3}  →  {rel}")

    if args.dry_run:
        print("[i] dry-run, saliendo.")
        return

    pending = [j for j in jobs if not j.skip]
    if not pending:
        print("[i] nada que generar.")
        return

    client = load_client()
    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    start = time.time()
    ok_count, fail_count = 0, 0

    if args.parallel <= 1:
        for j in pending:
            _, status = generate_one(client, j, args.skip_existing)
            rel = j.file_path.relative_to(OUT_ROOT)
            print(f"  [slide {j.slide}] {rel}  →  {status}")
            if status.startswith("OK") or status.startswith("CACHE") or status.startswith("SKIP"):
                ok_count += 1
            else:
                fail_count += 1
    else:
        with ThreadPoolExecutor(max_workers=args.parallel) as ex:
            futures = {
                ex.submit(generate_one, client, j, args.skip_existing): j
                for j in pending
            }
            for fut in as_completed(futures):
                j, status = fut.result()
                rel = j.file_path.relative_to(OUT_ROOT)
                print(f"  [slide {j.slide}] {rel}  →  {status}")
                if status.startswith("OK") or status.startswith("CACHE") or status.startswith("SKIP"):
                    ok_count += 1
                else:
                    fail_count += 1

    dt = time.time() - start
    print(f"[done] ok={ok_count} fail={fail_count} · {dt:.1f}s")


if __name__ == "__main__":
    main()
