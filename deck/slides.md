---
theme: default
title: uumami @ itam · esponda
info: |
  present time. present day.
  mario vázquez corte. dacc itam.
colorSchema: dark
class: 'theme-lain'
fonts:
  sans: 'Inter'
  mono: 'IBM Plex Mono'
  serif: 'Cinzel'
transition: fade
mdc: true
drawings:
  enabled: true
  persist: false
canvasWidth: 1280
---

<div class="cover-wrap">
  <img src="/img/01_uumami_cover.png" class="bg" onerror="this.style.display='none'" />
  <div class="grid-bg"></div>
  <MatrixRain />
  <div class="status-bar">
    <span class="dot-live"></span>
    <span>wired</span>
    <span class="sep">//</span>
    <span>present.day</span>
    <span class="sep">//</span>
    <span>online</span>
  </div>
  <div class="handle-big">
    <span class="u">u</span><span class="u">u</span><span class="u">m</span><span class="u">a</span><span class="u">m</span><span class="u">i</span><span class="cursor">▊</span>
  </div>
  <div class="sub"><Slashes :items="['present time', 'present day']" /></div>
  <div class="glyph tl">人</div>
  <div class="glyph tr">線</div>
  <div class="glyph bl">繋</div>
  <div class="glyph br">net</div>
  <div class="scan"></div>
  <div class="vignette"></div>
</div>

<style>
.cover-wrap {
  position: absolute; inset: 0;
  background:
    radial-gradient(ellipse at 70% 30%, rgba(127,255,181,0.08), transparent 55%),
    radial-gradient(ellipse at 20% 80%, rgba(255,46,195,0.06), transparent 50%),
    #0b0f0d;
  overflow: hidden;
}
.cover-wrap .bg {
  position: absolute; inset: 0; width: 100%; height: 100%;
  object-fit: cover; opacity: 0.75; z-index: 1;
}
.cover-wrap .grid-bg {
  position: absolute; inset: 0; z-index: 2;
  background-image:
    linear-gradient(rgba(127,255,181,0.08) 1px, transparent 1px),
    linear-gradient(90deg, rgba(127,255,181,0.08) 1px, transparent 1px);
  background-size: 80px 80px;
  mask-image: radial-gradient(ellipse at 50% 60%, black 10%, transparent 75%);
  pointer-events: none;
}
.cover-wrap > .matrix-rain {
  z-index: 3; opacity: 0.35; mix-blend-mode: screen;
}
.vignette {
  position: absolute; inset: 0; z-index: 6; pointer-events: none;
  background:
    radial-gradient(ellipse at 50% 50%, transparent 35%, rgba(11,15,13,0.6) 100%),
    linear-gradient(180deg, rgba(11,15,13,0.2) 0%, rgba(11,15,13,0.45) 100%);
}
.status-bar {
  position: absolute; top: 1.5rem; left: 2.5rem;
  z-index: 8;
  font-family: var(--font-mono);
  font-size: 0.8rem;
  color: var(--lain-fg);
  letter-spacing: 0.15em;
  display: flex; gap: 0.7rem; align-items: center;
  opacity: 0.88;
  text-transform: uppercase;
}
.dot-live {
  width: 8px; height: 8px; border-radius: 999px;
  background: var(--lain-fg);
  box-shadow: 0 0 10px var(--lain-fg);
  animation: pulse 1.4s ease-in-out infinite;
}
@keyframes pulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.4; transform: scale(0.7); }
}
.status-bar .sep { opacity: 0.35; }
.handle-big {
  position: absolute; top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  font-family: var(--font-mono); font-size: 7rem; font-weight: 300;
  color: var(--lain-fg); letter-spacing: 0.12em; z-index: 7;
  line-height: 1;
  display: flex; align-items: center;
}
.handle-big .u {
  display: inline-block;
  text-shadow:
    0 0 20px rgba(127,255,181,0.6),
    0 0 60px rgba(127,255,181,0.4),
    0 0 3px rgba(46,245,255,0.8);
  animation: flicker 6s infinite;
}
.handle-big .u:nth-child(2) { animation-delay: 0.3s; }
.handle-big .u:nth-child(3) { animation-delay: 0.6s; }
.handle-big .u:nth-child(4) { animation-delay: 0.9s; }
.handle-big .u:nth-child(5) { animation-delay: 1.2s; }
.handle-big .u:nth-child(6) { animation-delay: 1.5s; }
@keyframes flicker {
  0%, 100% { opacity: 1; }
  33% { opacity: 1; }
  34% { opacity: 0.65; }
  36% { opacity: 1; }
  50% { opacity: 1; }
  51% { opacity: 0.85; }
  52% { opacity: 1; }
}
.handle-big .cursor {
  margin-left: 0.15em;
  color: var(--lain-fg);
  animation: blink 1s steps(1) infinite;
}
@keyframes blink {
  0%, 49% { opacity: 1; }
  50%, 100% { opacity: 0; }
}
.cover-wrap .sub {
  position: absolute; bottom: 2.5rem; left: 50%;
  transform: translateX(-50%);
  z-index: 8;
  color: var(--lain-ink);
  font-family: var(--font-mono);
  font-size: 1.2rem;
  letter-spacing: 0.15em;
  opacity: 0.8;
}
.glyph {
  position: absolute;
  z-index: 7;
  font-family: var(--font-jp), var(--font-mono);
  color: var(--lain-fg);
  opacity: 0.5;
  font-size: 1.3rem;
  letter-spacing: 0.1em;
}
.glyph.tl { top: 1.5rem; right: 2.5rem; }
.glyph.tr { top: 40%; right: 2.5rem; font-size: 2.2rem; opacity: 0.18; }
.glyph.bl { bottom: 2rem; left: 2.5rem; font-size: 1.1rem; opacity: 0.6; }
.glyph.br { bottom: 2rem; right: 2.5rem; font-size: 0.8rem; opacity: 0.5; letter-spacing: 0.3em; }
.scan {
  position: absolute; inset: 0; z-index: 9; pointer-events: none;
  background: repeating-linear-gradient(
    0deg,
    rgba(0,0,0,0.22) 0px,
    rgba(0,0,0,0.22) 1px,
    transparent 1px,
    transparent 3px
  );
  mix-blend-mode: multiply;
}
</style>

---
layout: image-right
image: /img/avatar/base.png
class: 'theme-frieren layer-solarpunk'
---

# mario vázquez corte

<Slashes :items="['profe', 'data scientist', 'researcher', 'husbande']" />

<div class="kv mt-6">
  <div><span class="k">itam</span> · departamento académico de computación</div>
  <div><span class="k">desde</span> otoño 2025 · tiempo completo</div>
  <div><span class="k">handle</span> uumami · <a href="https://sonder.art" target="_blank">sonder.art</a></div>
  <div><span class="k">wiki</span> <a href="https://uumami.wiki" target="_blank">uumami.wiki</a></div>
</div>

---
layout: image-right
image: /img/03_que_hago.png
class: 'theme-lain layer-cyberpunk'
---

# qué hago

data science. eso es todo.

<div class="kv mt-6">
  <div><span class="k">industria</span> diseño sistemas de ia</div>
  <div><span class="k">academia</span> investigación y clases</div>
  <div><span class="k">ratos</span> construyo cosas raras</div>
</div>

---
layout: image-right
image: /img/vinlandia.png
class: 'theme-vinland layer-solarpunk'
---

# vinlandia

<div class="mt-6 quote">
  "a person from vinlandia.<br />
  nobody has enemies, only nakamas."
</div>

<div class="mt-10 tags">
  <span>absurdist</span>
  <span class="sep">·</span>
  <span>marxist-materialist</span>
  <span class="sep">·</span>
  <span>techno-communist</span>
</div>

<style>
.quote {
  font-family: var(--font-display);
  font-size: 1.35rem;
  line-height: 1.5;
  color: var(--vinland-fg);
  opacity: 0.95;
  max-width: 90%;
}
.tags {
  font-family: var(--font-mono);
  font-size: 1rem;
  letter-spacing: 0.05em;
  color: var(--vinland-ink);
  opacity: 0.9;
}
.tags .sep {
  color: var(--vinland-red);
  margin: 0 0.3em;
  opacity: 0.6;
}
</style>

---
layout: image-right
image: /img/mision.png
class: 'theme-eva layer-cyberpunk'
---

# misión

<div class="mt-4 mision">
  <div><span class="b">beat entropy</span></div>
  <div><span class="b">longevidad</span> — simular organismos vía omics + ia</div>
  <div><span class="b">p vs np</span> — si toca</div>
  <div><span class="b">inmortalidad</span> — para quien la quiera</div>
</div>

<div class="mt-8 kv">
  <div><span class="k">side-quests</span> videojuegos · novelas sci-fi · dune vi</div>
</div>

<style>
.mision {
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
  font-family: var(--font-mono);
  font-size: 1.15rem;
}
.mision .b {
  color: var(--eva-fg);
  font-weight: 500;
  margin-right: 0.5rem;
}
</style>

---
layout: default
class: 'theme-vinland layer-solarpunk'
---

# trayectoria

<div class="timeline">
  <div class="row">
    <span class="y">2011–2015</span>
    <span class="e">bs economía · itam · honors</span>
  </div>
  <div class="row">
    <span class="y">2016–2018</span>
    <span class="e">msc economic theory · itam · supervisor: romans pancs</span>
  </div>
  <div class="row">
    <span class="y">2017–2019</span>
    <span class="e">msc computer science · itam · honors · supervisor: luis montiel</span>
  </div>
  <div class="row">
    <span class="y">2017–2018</span>
    <span class="e">waltem · ds independiente · forecast tráfico naicm</span>
  </div>
  <div class="row">
    <span class="y">2018–2021</span>
    <span class="e">abraxas · sr ds → lead ds · pricing cinépolis, forecast bimbo</span>
  </div>
  <div class="row">
    <span class="y">2020–2024</span>
    <span class="e">amaru · co-founder / ex-cto · edtech + ia</span>
  </div>
  <div class="row">
    <span class="y">2021</span>
    <span class="e">paper mhar · <a href="https://arxiv.org/abs/2104.07097" target="_blank">arxiv 2104.07097</a></span>
  </div>
  <div class="row">
    <span class="y">2021–2023</span>
    <span class="e">superbio.ai · ai researcher / po · founding · seed 750k</span>
  </div>
  <div class="row">
    <span class="y">2023</span>
    <span class="e">mhar publicado · <a href="https://link.springer.com/article/10.1007/s00180-023-01411-y" target="_blank">springer computational statistics</a></span>
  </div>
  <div class="row">
    <span class="y">2023–2024</span>
    <span class="e">aleph · data scientist · detección de robo gps</span>
  </div>
  <div class="row">
    <span class="y">2023+</span>
    <span class="e">profesor itam · asignatura → tiempo completo otoño 2025</span>
  </div>
  <div class="row">
    <span class="y">2024–2025</span>
    <span class="e">onfire health · founding team lead · hoy advisor</span>
  </div>
  <div class="row">
    <span class="y">2025+</span>
    <span class="e">suggestic · data architect lead · cura · data dream solutions</span>
  </div>
</div>

<style>
.timeline {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.4rem 2.5rem;
  margin-top: 1rem;
  font-family: var(--font-mono);
  font-size: 0.9rem;
}
.row {
  display: flex;
  gap: 1rem;
  border-top: 1px solid rgba(215, 199, 163, 0.18);
  padding: 0.35rem 0;
  align-items: baseline;
}
.row .y {
  color: var(--vinland-red);
  flex-shrink: 0;
  min-width: 5.5rem;
  font-weight: 500;
}
.row .e {
  color: var(--vinland-ink);
  opacity: 0.92;
  line-height: 1.3;
}
</style>

---
layout: image-right
image: /img/roles.png
class: 'theme-lain layer-cyberpunk'
---

# roles

<div class="roles">
  <div class="r"><span class="name">ai architect</span><span class="what">diseñar sistemas de ia end-to-end</span></div>
  <div class="r"><span class="name">backender</span><span class="what">apis, colas, bases de datos, infra</span></div>
  <div class="r"><span class="name">data scientist</span><span class="what">modelo + experimento + decisión</span></div>
  <div class="r"><span class="name">cto</span><span class="what">dirección técnica · cura</span></div>
  <div class="r"><span class="name">cso</span><span class="what">chief science officer · cura</span></div>
  <div class="r"><span class="name">cdo</span><span class="what">chief data officer · data dream solutions</span></div>
</div>

<style>
.roles {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
  margin-top: 1rem;
  font-family: var(--font-mono);
}
.roles .r {
  padding: 0.4rem 0;
  border-bottom: 1px dashed rgba(127, 255, 181, 0.18);
  display: flex;
  flex-direction: column;
  gap: 0.15rem;
}
.roles .name {
  color: var(--lain-fg);
  font-size: 1.05rem;
  font-weight: 500;
  letter-spacing: 0.05em;
}
.roles .what {
  font-size: 0.9rem;
  opacity: 0.8;
}
</style>

---
layout: default
class: 'theme-lain layer-vaporwave'
---

# startups

<div class="companies">
  <div class="co"><span class="dot"></span> <b><a href="https://suggestic.com" target="_blank">suggestic</a></b> · data architect lead · chatbots, voz, food-lens</div>
  <div class="co"><span class="dot"></span> <b>cura</b> · cto + cso · hult prize 2026 ganador</div>
  <div class="co"><span class="dot"></span> <b>data dream solutions</b> · cdo · supply chain optimization e2e</div>
  <div class="co"><span class="dot"></span> <b><a href="https://onfirehealth.ai" target="_blank">onfire health</a></b> · founding team lead · advisor · backend+cloud+ia</div>
  <div class="co"><span class="dot"></span> <b><a href="https://superbio.ai" target="_blank">superbio.ai</a></b> · ai researcher / po · founding · ~50 apps bio-ml · seed 750k</div>
  <div class="co"><span class="dot"></span> <b><a href="https://aleph.app" target="_blank">aleph</a></b> · data scientist · detección robo vehículos vía gps</div>
  <div class="co"><span class="dot"></span> <b>abraxas</b> · lead ds · pricing cinépolis · forecast bimbo</div>
  <div class="co"><span class="dot"></span> <b>amaru</b> · co-founder / ex-cto · edtech · top 20 alibaba global</div>
  <div class="co"><span class="dot"></span> <b>waltem</b> · ds independiente · forecast naicm</div>
</div>

<img src="/img/05_startups.png" class="bg-right" />

<style>
.companies {
  margin-top: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  max-width: 68%;
  position: relative;
  z-index: 2;
}
.co {
  font-family: var(--font-mono);
  font-size: 0.95rem;
}
.co .dot {
  display: inline-block;
  width: 7px; height: 7px;
  border-radius: 999px;
  background: var(--vapor-mag);
  margin-right: 0.65rem;
  box-shadow: 0 0 8px var(--vapor-mag);
}
.co b {
  color: var(--vapor-cyan);
  font-weight: 500;
  letter-spacing: 0.03em;
}
.bg-right {
  position: absolute;
  right: 0;
  top: 0;
  height: 100%;
  width: 35%;
  object-fit: cover;
  opacity: 0.45;
  mask-image: linear-gradient(90deg, transparent 0%, black 30%);
  z-index: 0;
}
</style>

---
layout: default
class: 'theme-lain layer-cyberpunk'
---

# industria

<div class="dip">
  <img src="/img/06a_muro_industria.png" />
  <img src="/img/06b_mapa_mexico.png" />
</div>

<div class="dip-caption">
  cinépolis · bimbo · pochteca · naicm · nestlé · cenapred · bbva · ivim health · banks varios
</div>

<style>
.dip {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin-top: 1rem;
}
.dip img {
  width: 100%;
  height: 340px;
  object-fit: cover;
  border-radius: 4px;
  border: 1px solid rgba(0, 229, 255, 0.2);
}
.dip-caption {
  margin-top: 1rem;
  font-family: var(--font-mono);
  font-size: 0.9rem;
  opacity: 0.85;
  text-align: center;
  color: var(--cyber-cyan);
  letter-spacing: 0.04em;
}
</style>

---
layout: image-right
image: /img/avatar/research.png
class: 'theme-eva layer-cyberpunk'
---

# research

sí, escribí un paper. y otro.

<div class="kv mt-6">
  <div><span class="k">línea</span> mcmc · polytope sampling · gpu</div>
  <div><span class="k">claim</span> sampleador de polítopos más rápido del mundo</div>
  <div><span class="k">líneas activas</span> omics · scheduling · causalidad</div>
</div>

---
layout: default
class: 'theme-eva layer-cyberpunk'
---

# mhar

<div class="two">
  <div class="two-left">

muestrear puntos uniformes en una forma geométrica arbitraria.

usando matriz × matriz en lugar de vector × vector.

resultado: gpu. rápido. el más rápido, hasta donde sé.

<div class="kv mt-6">
  <div><span class="k">arxiv</span> <a href="https://arxiv.org/abs/2104.07097" target="_blank">2104.07097</a></div>
  <div><span class="k">springer</span> <a href="https://link.springer.com/article/10.1007/s00180-023-01411-y" target="_blank">computational statistics 2023</a></div>
  <div><span class="k">pypi</span> <a href="https://pypi.org/project/mhar" target="_blank">mhar</a></div>
</div>

  </div>
  <div class="two-right">
    <MharSampler />
  </div>
</div>

<style>
.two {
  display: grid;
  grid-template-columns: 1fr 1.3fr;
  gap: 2rem;
  align-items: center;
  margin-top: 1rem;
}
.two-left p { margin-bottom: 0.7rem; }
</style>

---
layout: image-right
image: /img/12_papers_omics.png
class: 'theme-eva layer-solarpunk'
---

# papers & líneas

<div class="papers">
  <div class="p">
    <div class="pt">mhar</div>
    <div class="pd">sampleador gpu · <a href="https://arxiv.org/abs/2104.07097" target="_blank">arxiv 2104.07097</a> · <a href="https://link.springer.com/article/10.1007/s00180-023-01411-y" target="_blank">springer 2023</a></div>
  </div>
  <div class="p">
    <div class="pt">minimal compromise</div>
    <div class="pd">teoría de elección · <a href="https://arxiv.org/abs/2010.08771" target="_blank">arxiv 2010.08771</a> · sen's β sin α</div>
  </div>
  <div class="p">
    <div class="pt">classroom assignment</div>
    <div class="pd">mapping al problema de matching</div>
  </div>
  <div class="p">
    <div class="pt">scheduling</div>
    <div class="pd">aplicación de sampling a optimización combinatoria</div>
  </div>
  <div class="p">
    <div class="pt">omics / genómica</div>
    <div class="pd">simular organismos · longevidad · benchmarks para modelos bio</div>
  </div>
</div>

<style>
.papers {
  margin-top: 0.8rem;
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
  font-family: var(--font-mono);
}
.papers .p {
  padding: 0.4rem 0;
  border-top: 1px dashed rgba(255, 58, 47, 0.2);
}
.papers .pt {
  color: var(--eva-fg);
  font-size: 1rem;
  font-weight: 500;
  letter-spacing: 0.04em;
  margin-bottom: 0.15rem;
}
.papers .pd {
  font-size: 0.85rem;
  opacity: 0.82;
  line-height: 1.4;
}
</style>

---
layout: image-right
image: /img/causalidad.png
class: 'theme-lain layer-cyberpunk'
---

# causalidad

no es sólo correlación.

<div class="kv mt-6">
  <div><span class="k">dag</span> directed acyclic graph · modelar qué causa qué</div>
  <div><span class="k">do-operator</span> intervención · ≠ observar</div>
  <div><span class="k">confounders</span> el enemigo silencioso</div>
  <div><span class="k">aplicación</span> pricing cinépolis · forecast bimbo · uplift</div>
</div>

<div class="mt-6 note">
  correlation ≠ causation. un modelo predictivo te dice qué pasa;
  un modelo causal te dice qué pasaría si tocas la palanca.
</div>

<style>
.note {
  font-family: var(--font-mono);
  font-size: 0.9rem;
  line-height: 1.4;
  opacity: 0.78;
  border-left: 2px solid var(--cyber-cyan);
  padding-left: 0.8rem;
  max-width: 90%;
}
</style>

---
layout: image-right
image: /img/avatar/victory.png
class: 'theme-elden layer-solarpunk'
---

# cura

<div class="kv mt-6">
  <div><span class="k">rol</span> cto + chief science officer</div>
  <div><span class="k">2026</span> hult prize · ganador</div>
  <div><span class="k">qué</span> asistente para cuidadores de pacientes con demencia</div>
</div>

<div class="mt-6 chips">
  <span class="chip">llms</span>
  <span class="chip">voz</span>
  <span class="chip">rag</span>
  <span class="chip">health</span>
  <span class="chip">lat-am</span>
</div>

---
layout: default
class: 'theme-elden layer-solarpunk'
---

# nestlé

<div class="triple">
  <figure>
    <img src="/img/10a_maira.png" />
    <figcaption>
      <b><a href="https://malnutrition-face-scanner.vercel.app/" target="_blank">maira</a></b>
      <span>detección de malnutrición por foto · patente en trámite</span>
    </figcaption>
  </figure>
  <figure>
    <img src="/img/10b_amanda.png" />
    <figcaption>
      <b><a href="https://nuco.ai/hcp" target="_blank">amanda</a></b>
      <span>chatbot para pacientes con alimentación por sonda</span>
    </figcaption>
  </figure>
  <figure>
    <img src="/img/10c_foodlens.png" />
    <figcaption>
      <b>food-lens</b>
      <span>macros por foto · ganó benchmark 5k-calorie</span>
    </figcaption>
  </figure>
</div>

<style>
.triple {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin-top: 1rem;
}
.triple figure { margin: 0; }
.triple img {
  width: 100%;
  height: 240px;
  object-fit: cover;
  border-radius: 4px;
  border: 1px solid rgba(201, 161, 89, 0.3);
}
.triple figcaption {
  margin-top: 0.6rem;
  font-family: var(--font-mono);
  font-size: 0.85rem;
  line-height: 1.4;
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
}
.triple figcaption b {
  color: var(--elden-fg);
  font-weight: 500;
  letter-spacing: 0.05em;
}
.triple figcaption span { opacity: 0.82; }
</style>

---
layout: default
class: 'theme-lain layer-cyberpunk'
---

# chatbots

<div class="chatbots-grid">
  <div class="chatbots-left">

<div class="arch">
  <div class="step"><span class="n">01</span> asr · speech → text</div>
  <div class="step"><span class="n">02</span> intent · nlu + memoria</div>
  <div class="step"><span class="n">03</span> retrieval · rag sobre docs</div>
  <div class="step"><span class="n">04</span> llm · generación</div>
  <div class="step"><span class="n">05</span> guardrails · safety, tono, tools</div>
  <div class="step"><span class="n">06</span> tts · text → speech</div>
</div>

<div class="mt-3 kv">
  <div><span class="k">prod</span> suggestic · <a href="https://nuco.ai/hcp" target="_blank">amanda</a> · cura · suvi</div>
</div>

  </div>
  <div class="chatbots-right">
    <ChatbotMini />
  </div>
</div>

<style>
.chatbots-grid {
  display: grid;
  grid-template-columns: 1fr 1.2fr;
  gap: 1.5rem;
  margin-top: 0.5rem;
  align-items: start;
}
.arch {
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
  font-family: var(--font-mono);
  font-size: 0.9rem;
}
.arch .step {
  display: flex;
  gap: 0.7rem;
  padding: 0.25rem 0;
  border-bottom: 1px dashed rgba(127, 255, 181, 0.18);
}
.arch .n {
  color: var(--lain-fg);
  min-width: 1.6rem;
  font-weight: 500;
}
</style>

---
layout: default
class: 'theme-lain layer-cyberpunk'
---

# rag

<div class="rag-grid">
  <div class="rag-left">

retrieval augmented generation.

<div class="arch mt-3">
  <div class="step"><span class="n">01</span> chunkear</div>
  <div class="step"><span class="n">02</span> embeddings</div>
  <div class="step"><span class="n">03</span> vector store · faiss · qdrant · pgvector</div>
  <div class="step"><span class="n">04</span> top-k · similitud coseno / jaccard</div>
  <div class="step"><span class="n">05</span> rerank</div>
  <div class="step"><span class="n">06</span> contexto → llm</div>
</div>

<div class="mt-3 note">
  el llm no sabe lo que tú sabes. rag le da los docs correctos.
  evita alucinaciones si se hace bien.
</div>

  </div>
  <div class="rag-right">
    <RagRetrieval />
  </div>
</div>

<style>
.rag-grid {
  display: grid;
  grid-template-columns: 0.8fr 1.4fr;
  gap: 1.5rem;
  margin-top: 0.4rem;
  align-items: start;
}
</style>

---
layout: default
class: 'theme-eva layer-cyberpunk'
---

# agentic engineering

<div class="agent-grid">
  <div class="agent-left">

agentes que deciden, no sólo responden.

<div class="kv mt-3">
  <div><span class="k">tool use</span> el modelo llama funciones</div>
  <div><span class="k">loops</span> plan → act → observe → repeat</div>
  <div><span class="k">harness</span> orquestador del loop</div>
  <div><span class="k">control flow</span> quién decide y cuándo</div>
</div>

<div class="mt-3 note">
  un chatbot responde. un agente actúa. la diferencia es quién tiene
  las llaves del auto.
</div>

  </div>
  <div class="agent-right">
    <AgentLoop />
  </div>
</div>

<style>
.agent-grid {
  display: grid;
  grid-template-columns: 0.8fr 1.5fr;
  gap: 1.5rem;
  margin-top: 0.4rem;
  align-items: start;
}
</style>

---
layout: image-right
image: /img/harnesses.png
class: 'theme-eva layer-cyberpunk'
---

# harnesses / evals

cómo sabes si tu modelo está bien.

<div class="kv mt-4">
  <div><span class="k">unit tests</span> sí, para prompts también</div>
  <div><span class="k">benchmarks</span> hellaswag · mmlu · tu propio set</div>
  <div><span class="k">judge model</span> un llm evalúa al otro</div>
  <div><span class="k">human eval</span> caro pero necesario</div>
  <div><span class="k">regresión</span> no romper lo que ya funciona</div>
</div>

<div class="mt-4 note">
  "vibes" no es un método. si no lo mides, no existe.
</div>

---
layout: default
class: 'theme-lain layer-vaporwave'
---

# proyectos vibe

lo que hago cuando nadie me paga.

<div class="vibe-grid">
  <figure>
    <img src="/img/11a_lain_shell.png" />
    <figcaption><b><a href="https://github.com/uumami/lain-shell" target="_blank">lain-shell</a></b><span>shell en rust · present day</span></figcaption>
  </figure>
  <figure>
    <img src="/img/11b_raya_lucaria.png" />
    <figcaption><b><a href="https://uumami.wiki/raya_lucaria/" target="_blank">raya lucaria</a></b><span>plataforma de cursos · glintstone engine</span></figcaption>
  </figure>
  <figure>
    <img src="/img/11c_tycoon_points.png" />
    <figcaption><b>tycoon points</b><span>quant research en tiempo muerto</span></figcaption>
  </figure>
</div>

<style>
.vibe-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin-top: 1rem;
}
.vibe-grid figure { margin: 0; }
.vibe-grid img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 4px;
  border: 1px solid rgba(46, 245, 255, 0.2);
}
.vibe-grid figcaption {
  margin-top: 0.5rem;
  font-family: var(--font-mono);
  font-size: 0.85rem;
  line-height: 1.35;
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
}
.vibe-grid figcaption b {
  color: var(--vapor-cyan);
  font-weight: 500;
  letter-spacing: 0.04em;
}
.vibe-grid figcaption span { opacity: 0.8; }
</style>

---
layout: center
class: 'theme-lain layer-vaporwave'
title: terminal
---

<LainTerminal />

---
layout: default
class: 'theme-elden layer-solarpunk'
---

# raya lucaria

<div class="rl-grid">
  <div class="rl-left">

plataforma de cursos con grafo interactivo de conocimiento.

<div class="kv mt-4">
  <div><span class="k">engine</span> glintstone · 11ty + tailwind + docker</div>
  <div><span class="k">features</span> grafo force/jerarquía/circular · search · katex · mermaid</div>
  <div><span class="k">uso</span> mis cursos de itam + otros profes</div>
  <div><span class="k">live</span> <a href="https://uumami.wiki/raya_lucaria/grafo/" target="_blank">uumami.wiki/raya_lucaria/grafo/</a></div>
</div>

  </div>
  <div class="rl-right">
    <iframe
      src="https://uumami.wiki/raya_lucaria/grafo/"
      loading="lazy"
      referrerpolicy="no-referrer"
      allow="autoplay; encrypted-media"
    ></iframe>
    <div class="rl-fallback">
      <img src="/img/11b_raya_lucaria.png" />
    </div>
  </div>
</div>

<style>
.rl-grid {
  display: grid;
  grid-template-columns: 1fr 1.4fr;
  gap: 1.5rem;
  margin-top: 0.6rem;
  align-items: stretch;
}
.rl-right {
  position: relative;
  border-radius: 4px;
  overflow: hidden;
  border: 1px solid rgba(201, 161, 89, 0.3);
  min-height: 400px;
  background: var(--elden-bg);
}
.rl-right iframe {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  border: 0;
  z-index: 2;
}
.rl-fallback {
  position: absolute;
  inset: 0;
  z-index: 1;
}
.rl-fallback img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0.7;
}
</style>

---
layout: image-right
image: /img/avatar/teacher.png
class: 'theme-frieren layer-solarpunk'
---

# clases

<div class="classes">
  <div class="course">
    <div class="cname">inteligencia artificial</div>
    <div class="cdesc">fundamentos · de la percepción al agente</div>
  </div>
  <div class="course">
    <div class="cname">fuentes de datos</div>
    <div class="cdesc">sql · apis · scraping · pipelines</div>
  </div>
  <div class="course">
    <div class="cname">chatbots / automl</div>
    <div class="cdesc">llms · rag · agentes · automl</div>
  </div>
</div>

<div class="evals mt-6">
  <span class="k">promedio eval</span> 4.74 · <span class="k">alumnos</span> 165 · <span class="k">cursos</span> 10
</div>

<style>
.classes {
  margin-top: 0.8rem;
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}
.course {
  padding: 0.6rem 0.9rem;
  border-left: 3px solid var(--frieren-gold);
  background: rgba(201, 161, 89, 0.06);
}
.cname {
  font-family: var(--font-display);
  font-size: 1.15rem;
  color: var(--frieren-ink);
  letter-spacing: 0.03em;
}
.cdesc {
  margin-top: 0.15rem;
  font-family: var(--font-mono);
  font-size: 0.82rem;
  opacity: 0.82;
  color: var(--frieren-ink);
}
.evals {
  font-family: var(--font-mono);
  font-size: 0.9rem;
  color: var(--frieren-ink);
  opacity: 0.82;
}
.evals .k { color: var(--frieren-gold); margin-right: 0.25rem; }
</style>

---
layout: image-right
image: /img/13_ds_real.png
class: 'theme-eva layer-cyberpunk'
---

# qué hace un ds real

no es kaggle. no son tableros bonitos.

<div class="flow mt-4">
  <div>1. alguien tiene un problema</div>
  <div>2. no saben qué datos tienen</div>
  <div>3. los datos están mal</div>
  <div>4. los arreglas</div>
  <div>5. modelo, a veces</div>
  <div>6. convences a alguien de usarlo</div>
  <div>7. mantenerlo vivo es el 80% del trabajo</div>
</div>

<style>
.flow {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  font-family: var(--font-mono);
  font-size: 0.95rem;
}
.flow > div {
  padding: 0.3rem 0;
  border-bottom: 1px dashed rgba(255, 58, 47, 0.2);
}
</style>

---
layout: default
class: 'theme-vinland layer-solarpunk'
---

# día típico

<img src="/img/14_dia_tipico.png" class="banner" />

<div class="day">
  <div class="hour"><span class="h">08</span> café, arxiv, inbox</div>
  <div class="hour"><span class="h">10</span> junta con producto o cliente</div>
  <div class="hour"><span class="h">12</span> código · experimentos · debugging</div>
  <div class="hour"><span class="h">15</span> revisar modelos en prod</div>
  <div class="hour"><span class="h">17</span> clase o asesoría de tesis</div>
  <div class="hour"><span class="h">20</span> side-project · lain-shell, tycoon, omics</div>
</div>

<style>
.banner {
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-radius: 4px;
  margin-top: 0.6rem;
  margin-bottom: 1rem;
  opacity: 0.85;
}
.day {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.6rem 2rem;
}
.hour {
  font-family: var(--font-mono);
  font-size: 0.95rem;
  display: flex;
  gap: 0.8rem;
}
.hour .h {
  color: var(--vinland-red);
  font-weight: 600;
  min-width: 2rem;
}
</style>

---
layout: default
class: 'theme-elden layer-vaporwave'
---

# skills

<div class="skills-quiz">
  <div class="skills">
    <div class="skill">matemáticas<span>álgebra lineal · prob · estadística · optimización</span></div>
    <div class="skill">código<span>python · sql · git · después lo demás</span></div>
    <div class="skill">inglés<span>para leer papers y no quedarte atrás</span></div>
    <div class="skill">escribir<span>bien. en serio.</span></div>
    <div class="skill">construir<span>enviar cosas. no sólo teoría.</span></div>
    <div class="skill">leer<span>un paper al día · una semana al mes para side-projects</span></div>
  </div>
  <div class="quiz-col">
    <RolQuiz />
  </div>
</div>

<style>
.skills-quiz {
  display: grid;
  grid-template-columns: 0.9fr 1.5fr;
  gap: 2rem;
  margin-top: 0.5rem;
}
.skill {
  font-family: var(--font-mono);
  padding: 0.35rem 0;
  border-bottom: 1px dashed rgba(201, 161, 89, 0.22);
  display: flex;
  flex-direction: column;
  gap: 0.15rem;
  font-size: 1rem;
  color: var(--elden-fg);
  letter-spacing: 0.04em;
}
.skill span {
  font-size: 0.8rem;
  color: var(--elden-ink);
  opacity: 0.78;
  font-weight: 400;
  letter-spacing: 0;
}
</style>

---
layout: image-right
image: /img/16_consejo.png
class: 'theme-eva layer-solarpunk'
---

# consejo

no tienes que ser genio.

<div class="advice mt-6">
  <div>envía</div>
  <div>pregunta</div>
  <div>lee</div>
  <div>repite</div>
</div>

<div class="kv mt-8">
  <div><span class="k">el truco</span> hacerlo por años, no por semanas</div>
</div>

<style>
.advice {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
  font-family: var(--font-display);
  font-size: 2.8rem;
  font-weight: 500;
  letter-spacing: 0.02em;
  color: var(--eva-fg);
  line-height: 1;
}
</style>

---
layout: image-right
image: /img/17_contacto.png
class: 'theme-lain layer-cyberpunk'
---

# contacto

<div class="ct-grid">
  <div class="contact">
    <div class="row"><span class="k">wiki</span> <a href="https://uumami.wiki" target="_blank">uumami.wiki</a></div>
    <div class="row"><span class="k">github</span> <a href="https://github.com/uumami" target="_blank">github.com/uumami</a></div>
    <div class="row"><span class="k">email</span> <a href="mailto:uumami@sonder.art">uumami@sonder.art</a></div>
    <div class="row"><span class="k">itam</span> <a href="mailto:mario.vazquez.corte@itam.mx">mario.vazquez.corte@itam.mx</a></div>
    <div class="row mt-4"><span class="k">esta presentación</span> <a href="https://uumami.wiki/presentacion_clase_esponda/" target="_blank">uumami.wiki/presentacion_clase_esponda</a></div>
  </div>
  <div class="qr-wrap">
    <QrcodeVue
      value="https://uumami.wiki/presentacion_clase_esponda/"
      :size="240"
      level="H"
      background="#0b0f0d"
      foreground="#7fffb5"
    />
    <div class="qr-caption">escanea y ábrelo</div>
  </div>
</div>

<div class="end mt-10">
  <Slashes :items="['preguntas', 'lo que sea']" />
</div>

<script setup>
import QrcodeVue from 'qrcode.vue'
</script>

<style>
.ct-grid {
  margin-top: 1.2rem;
  display: grid;
  grid-template-columns: 1fr max-content;
  gap: 3rem;
  align-items: start;
}
.contact {
  display: flex;
  flex-direction: column;
  gap: 0.55rem;
  font-family: var(--font-mono);
  font-size: 1.1rem;
}
.contact .row .k {
  color: var(--lain-fg);
  margin-right: 1rem;
  font-weight: 500;
  min-width: 9rem;
  display: inline-block;
}
.qr-wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.6rem;
  padding: 0.7rem;
  border: 1px solid rgba(127, 255, 181, 0.25);
  border-radius: 6px;
  background: rgba(11, 15, 13, 0.6);
}
.qr-caption {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  opacity: 0.7;
  letter-spacing: 0.1em;
}
.end {
  font-size: 1.1rem;
  opacity: 0.55;
}
</style>
