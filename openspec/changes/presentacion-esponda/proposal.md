# presentacion-esponda

## context

presentación de uumami (mario vázquez corte) para la clase de esponda en itam. 90 min, segundo semestre. objetivo: que los alumnos entiendan qué hace un data scientist en el mundo real y quieran ser uno, usando a uumami como caso vivo. shock visual alto, copy minimalista, sin cringe.

## goals

- deck desplegable y reproducible (slidev + gh pages)
- identidad visual fuerte: lain/eva/frieren/vinland/elden × vaporwave/cyberpunk/solarpunk
- avatar recurrente uumami (reemplazo de foto real)
- 3 interactivos en vivo: muestreo mhar, terminal estilo lain-shell, rol selector
- prompts.txt ordenado para regenerar imágenes con gemini nano banana
- script python que lee prompts.txt y genera pngs vía google-genai

## non-goals

- no usar foto real del usuario
- no incluir iframes dependientes de internet del aula (todo bundled)
- no ser un tutorial de ds — es una charla
- no incluir voz "motivadora" con signos de exclamación ni preguntas retóricas tipo "¿quién soy?"

## deliverables

- `openspec/changes/presentacion-esponda/{proposal,design,tasks}.md`
- `prompts/nano_banana_prompts.txt`
- `scripts/generate_images.py`
- `deck/` slidev project completo: `slides.md`, `package.json`, componentes vue, theme paths
- `deck/public/img/` donde aterriza nano banana
- `README.md` en raíz con instrucciones de generación + build + deploy
- `.github/workflows/deploy.yml` para gh pages

## timeline

deadline: mañana (2026-04-24). scope mínimo viable primero: scaffold + slides.md + prompts.txt. interactivos y deploy después si alcanza.
