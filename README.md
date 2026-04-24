# presentacion-esponda

presentación de uumami (mario vázquez corte) para la clase de esponda · itam · 90 min · segundo semestre.

stack: **slidev** (vue + markdown) · imágenes generadas con **gemini 2.5 flash image** (nano banana) · deploy a **github pages**.

## quickstart

### 1. generar imágenes

necesitas una api key de gemini.

```bash
export GEMINI_API_KEY=...            # o GOOGLE_API_KEY
python3 scripts/generate_images.py   # ~4 min en serial
# o en paralelo:
python3 scripts/generate_images.py --parallel 3

# solo una slide:
python3 scripts/generate_images.py --only 08

# no regenerar si ya existen:
python3 scripts/generate_images.py --skip-existing

# solo listar qué haría:
python3 scripts/generate_images.py --dry-run
```

las imágenes aterrizan en `deck/public/img/` en las rutas de `File:` que aparecen en `prompts/nano_banana_prompts.txt`.

### 2. correr el deck

```bash
cd deck
pnpm install
pnpm dev     # abre en http://localhost:3030
```

### 3. build estático

```bash
cd deck
pnpm build
# salida: deck/dist/
```

### 4. export a pdf

```bash
cd deck
pnpm install -D playwright-chromium
pnpm export   # salida: deck/slides-export.pdf
```

## estructura

```
presentacion_clase_esponda/
├── README.md                    ← este archivo
├── openspec/changes/presentacion-esponda/
│   ├── proposal.md              ← qué y por qué
│   ├── design.md                ← cómo (stack, paletas, pacing)
│   └── tasks.md                 ← checklist
├── prompts/
│   └── nano_banana_prompts.txt  ← 22 prompts ordenados por slide
├── scripts/
│   └── generate_images.py       ← parser + generador
├── deck/
│   ├── package.json
│   ├── slides.md                ← 17 slides en markdown
│   ├── style.css                ← paletas lain/eva/frieren/vinland/elden
│   ├── components/              ← componentes vue custom
│   │   ├── CrtFrame.vue
│   │   ├── FloatingAvatar.vue
│   │   ├── LainTerminal.vue
│   │   ├── MharSampler.vue
│   │   ├── RolQuiz.vue
│   │   └── Slashes.vue
│   └── public/img/              ← aquí aterriza nano banana
└── .github/workflows/deploy.yml ← gh pages
```

## slides y estética

17 slides + 3 interactivos. paleta × slide en `openspec/changes/presentacion-esponda/design.md`. cada slide usa una mezcla de **ancla anime/juego** (lain / eva / frieren / vinland / elden / snk / one piece / 3bp / dune) × **capa gráfica** (vaporwave / cyberpunk / solarpunk).

interactivos:

- **slide 08 — `<MharSampler />`** : canvas 2d samplea puntos uniformes en un triángulo vía hit-and-run, paso a paso.
- **slide 11b — `<LainTerminal />`** : terminal fake estilo lain-shell con prompt verde fósforo, escribe comandos scripted.
- **slide 15 — `<RolQuiz />`** : selector de rol (analyst / mle / researcher / founder) con reveal de bullets.

## deploy a github pages

1. push a un repo público en github (`uumami/presentacion-esponda` o similar).
2. en settings → pages → source: **github actions**.
3. el workflow `.github/workflows/deploy.yml` corre automáticamente en push a `main`.

el `--base` path del build está seteado a `/presentacion-esponda/` — ajústalo en `deck/package.json` si el repo se llama distinto.

## voz del copy

minúsculas, slashes, seca. no signos de exclamación. no preguntas retóricas tipo "¿quién soy?". ver `memory/user_voice.md` si hace falta iterar.

## troubleshooting

- **imágenes no se ven en dev**: asegurar que `deck/public/img/` existe y tiene los pngs. el script los pone ahí.
- **falta api key**: el script te avisa. `export GEMINI_API_KEY=...`.
- **una imagen salió fea**: re-corre solo esa slide con `--only XX`; el script limpia el cache automáticamente si el prompt cambió.
- **pnpm install falla**: prueba `npm install` como fallback.
