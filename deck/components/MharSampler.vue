<template>
  <div class="mhar">
    <canvas ref="canvasRef" :width="w" :height="h" />
    <div class="mhar-hud">
      <div class="kv"><span class="k">samples</span> {{ count }}</div>
      <div class="kv"><span class="k">step</span> {{ step }}</div>
      <button @click="toggle">{{ running ? 'pause' : 'run' }}</button>
      <button @click="reset">reset</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const w = 720;
const h = 560;

const canvasRef = ref(null);
const count = ref(0);
const step = ref(0);
const running = ref(false);
let raf = null;
let ctx = null;
let current = null;

// triangle vertices (2-simplex)
const V = [
  { x: 360, y: 80 },
  { x: 80, y: 500 },
  { x: 640, y: 500 },
];

function pointInTriangle(p) {
  const d = (a, b, c) =>
    (a.x - c.x) * (b.y - c.y) - (b.x - c.x) * (a.y - c.y);
  const d1 = d(p, V[0], V[1]);
  const d2 = d(p, V[1], V[2]);
  const d3 = d(p, V[2], V[0]);
  const hasNeg = d1 < 0 || d2 < 0 || d3 < 0;
  const hasPos = d1 > 0 || d2 > 0 || d3 > 0;
  return !(hasNeg && hasPos);
}

function drawTriangle() {
  ctx.strokeStyle = '#c9a159';
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.moveTo(V[0].x, V[0].y);
  ctx.lineTo(V[1].x, V[1].y);
  ctx.lineTo(V[2].x, V[2].y);
  ctx.closePath();
  ctx.stroke();
}

function clear() {
  ctx.fillStyle = '#0a0511';
  ctx.fillRect(0, 0, w, h);
  drawTriangle();
}

function randomInterior() {
  // rejection sampling
  while (true) {
    const p = { x: Math.random() * w, y: Math.random() * h };
    if (pointInTriangle(p)) return p;
  }
}

function hitAndRunStep(p) {
  // pick random direction, walk to boundary in both directions, sample uniformly on segment
  const theta = Math.random() * Math.PI * 2;
  const dx = Math.cos(theta);
  const dy = Math.sin(theta);
  // binary search for boundary in +dir and -dir
  let tPlus = 0, tMinus = 0;
  for (let s = 1; s < 800; s += 2) {
    if (pointInTriangle({ x: p.x + dx * s, y: p.y + dy * s })) tPlus = s;
    else break;
  }
  for (let s = 1; s < 800; s += 2) {
    if (pointInTriangle({ x: p.x - dx * s, y: p.y - dy * s })) tMinus = s;
    else break;
  }
  const t = -tMinus + Math.random() * (tPlus + tMinus);
  return { x: p.x + dx * t, y: p.y + dy * t };
}

function tick() {
  if (!running.value) return;
  for (let i = 0; i < 3; i++) {
    current = hitAndRunStep(current);
    ctx.fillStyle = 'rgba(127, 255, 181, 0.85)';
    ctx.beginPath();
    ctx.arc(current.x, current.y, 1.6, 0, Math.PI * 2);
    ctx.fill();
    count.value++;
    step.value++;
  }
  raf = requestAnimationFrame(tick);
}

function toggle() {
  running.value = !running.value;
  if (running.value) tick();
  else if (raf) cancelAnimationFrame(raf);
}

function reset() {
  count.value = 0;
  step.value = 0;
  current = randomInterior();
  clear();
}

onMounted(() => {
  ctx = canvasRef.value.getContext('2d');
  current = randomInterior();
  clear();
});

onUnmounted(() => {
  if (raf) cancelAnimationFrame(raf);
});
</script>

<style scoped>
.mhar {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  align-items: flex-start;
}
canvas {
  border: 1px solid rgba(201, 161, 89, 0.3);
  border-radius: 4px;
  background: #0a0511;
}
.mhar-hud {
  display: flex;
  gap: 1.5rem;
  align-items: center;
  font-family: var(--font-mono);
  font-size: 0.9rem;
}
.mhar-hud button {
  background: transparent;
  border: 1px solid var(--eva-fg);
  color: var(--eva-fg);
  padding: 0.3rem 0.9rem;
  font-family: var(--font-mono);
  font-size: 0.85rem;
  cursor: pointer;
  border-radius: 3px;
  text-transform: lowercase;
}
.mhar-hud button:hover {
  background: var(--eva-fg);
  color: var(--eva-bg);
}
.kv .k { color: var(--eva-fg); margin-right: 0.5rem; }
</style>
