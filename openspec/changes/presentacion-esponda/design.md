# design — presentacion-esponda

## stack

| capa | elección | por qué |
|---|---|---|
| deck | **slidev** (vue + markdown) | markdown fast, componentes vue para drip custom, monaco editor built-in, drawings en vivo, presenter mode con timer |
| build | vite (incluido en slidev) | — |
| styles | unocss (slidev default) + css vars | paletas cambiables por slide |
| imgs | **gemini 2.5 flash image** (nano banana) vía `google-genai` 1.61 | ya instalado, soporta text-in-image y 16:9 |
| deploy | gh pages vía `slidev build --base` + actions | ya tiene experiencia desde raya_lucaria |
| python | 3.10 ya instalado | script de generación |

## estructura del repo

```
presentacion_clase_esponda/
├── README.md
├── openspec/changes/presentacion-esponda/
│   ├── proposal.md  design.md  tasks.md
├── prompts/
│   └── nano_banana_prompts.txt
├── scripts/
│   └── generate_images.py
├── deck/
│   ├── package.json
│   ├── slides.md
│   ├── components/
│   │   ├── CrtFrame.vue
│   │   ├── MharSampler.vue
│   │   ├── LainTerminal.vue
│   │   └── RolQuiz.vue
│   ├── layouts/
│   │   ├── lain.vue
│   │   ├── eva.vue
│   │   ├── frieren.vue
│   │   ├── vinland.vue
│   │   └── elden.vue
│   ├── style.css
│   └── public/
│       └── img/
│           ├── 01_uumami_cover.png
│           ├── ...
│           └── avatar/
│               ├── base.png
│               ├── research.png
│               ├── victory.png
│               └── teacher.png
└── .github/workflows/deploy.yml
```

## paletas

```
--lain-bg      #0b0f0d   --lain-fg      #7fffb5   --lain-ink    #e8fff3
--eva-bg       #0a0511   --eva-fg       #ff3a2f   --eva-amber   #f7b500
--frieren-bg  #e8ecf0   --frieren-fg  #5a6b8a   --frieren-sil #c9d4e0
--vinland-bg  #14100c   --vinland-fg  #d7c7a3   --vinland-red #8b2d2d
--elden-bg    #1a1410   --elden-fg    #c9a159   --elden-ink   #e8d9b0

--vapor-mag   #ff2ec3   --vapor-cyan  #2ef5ff   --vapor-viol #a64dff
--cyber-red   #ff0044   --cyber-cyan  #00e5ff   --cyber-amber #ff9f1c
--solar-green #6ab04c   --solar-gold  #f7b500   --solar-rust #c76e3a
```

## avatar system

un solo personaje, 4 variantes. bob-cut oscuro estilo lain masculino, lentes cuadrados gruesos, playera negra. se reusa en esquina inferior derecha de slides clave como "guía" tipo vtuber/mentor.

- `avatar/base.png` — neutral, frente, busto
- `avatar/research.png` — pensativo, runas flotantes (slide mhar)
- `avatar/victory.png` — puño arriba, oro (slide cura)
- `avatar/teacher.png` — frieren-maga con libro (slide clases)

## paleta × slide (ancla anime × capa gráfica × #imgs)

```
01 uumami          lain × vaporwave        1 full bleed
02 mario           frieren × solarpunk     1 (avatar base)
03 qué hago        lain × cyberpunk        1
04 trayectoria     vinland × solarpunk     1 erdtree timeline
05 startups        one piece × vaporwave   1 banderas
06 industria       snk × cyberpunk         2 (muro + mapa)
07 research (intro) eva × cyberpunk        1 (avatar research)
08 mhar            eva × cyberpunk         1 + demo canvas
09 cura            elden × solarpunk       1 (avatar victory)
10 nestlé          elden × solarpunk       3 (maira/amanda/foodlens)
11 vibe projects   lain × vaporwave        3 tríptico + demo terminal
12 clases          frieren × solarpunk     1 (avatar teacher)
13 rol real        3bp × cyberpunk         1
14 día típico      dune × solarpunk        1
15 skills          elden × vaporwave       1 + mini quiz
16 consejo         eva × solarpunk         1
17 contacto        lain × cyberpunk        1
```

## interactivos

1. **MharSampler.vue** — canvas 2d, triángulo regular (símplex 2-simplex proyectado), puntos samplados paso-a-paso al tocar espacio. demuestra que "random" uniforme en formas no triviales es un problema no trivial. 0 dependencias externas.
2. **LainTerminal.vue** — fake shell con prompt `uumami@wired:~$`, scripted. escribe comandos ficticios con `setTimeout`, muestra output en verde fósforo. comandos: `cat ~/about.md`, `ls projects/`, `echo $DREAM`. puro css + js, fuente monospace.
3. **RolQuiz.vue** — 4 opciones (analyst, mle, researcher, founder). click → reveal. cada rol con 3 bullets de qué hace y una imagen anime mini.

## pacing 90 min

```
00:00 (5')  intro — 01, 02
00:05 (10') qué hago + trayectoria — 03, 04, 05
00:15 (10') industria — 06, 07
00:25 (10') research — 08 + DEMO mhar
00:35 (5')  cura — 09
00:40 (15') nestlé + vibe — 10, 11 + DEMO terminal
00:55 (5')  clases — 12
01:00 (10') rol real + día — 13, 14
01:10 (7')  skills — 15 + QUIZ
01:17 (3')  consejo — 16
01:20 (10') contacto + q&a — 17
```

## riesgos

- **api key de gemini no está en env.** el script saldrá con instrucciones claras; user setea `GEMINI_API_KEY` o `GOOGLE_API_KEY` y corre.
- **rendering de 20 imágenes**: ~4 min en serial, asumiendo 10s por imagen. batch de 3 en paralelo si el usuario quiere acelerar.
- **aula sin internet**: deck bundled, no depende de iframes externos. fallback para imágenes que no se generaron: css-only placeholders con paleta.
- **tiempo total**: 90 min es largo. hay que ensayar pacing hoy noche.

## voice del copy (ya memorizado)

lowercase, slash-descriptors, sin signos de exclamación, sin preguntas retóricas, escala grande dicha seca. ver `memory/user_voice.md`.
