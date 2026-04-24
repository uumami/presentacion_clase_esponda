<template>
  <div class="global-ui">
    <!-- top-right: live session clock -->
    <div class="session">
      <span class="dot-live"></span>
      <span class="label">wired</span>
      <span class="sep">//</span>
      <span class="time">{{ clock }}</span>
    </div>

    <!-- bottom-right: ASCII sprite cycling -->
    <div class="sprite">{{ currentSprite }}</div>

    <!-- bottom: scrolling ticker -->
    <div class="ticker">
      <div class="ticker-track">
        <span v-for="(t, i) in tickerLoop" :key="i" class="item">
          <span class="txt">{{ t }}</span>
          <span class="sep">//</span>
        </span>
      </div>
    </div>

    <!-- ambient floating glyphs -->
    <div class="ambient">
      <span v-for="g in glyphs" :key="g.id" class="glyph" :style="g.style">{{ g.char }}</span>
    </div>

    <!-- random glitch flash -->
    <div class="glitch" :class="{ active: glitching }"></div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'

// ========================================
// session clock
// ========================================
const clock = ref('')
let clockTimer = null
function tickClock() {
  const d = new Date()
  clock.value = d.toLocaleTimeString('es-MX', { hour12: false })
}

// ========================================
// ASCII sprite cycler
// ========================================
const spriteFrames = [
  'ヽ(°◇° )ノ',
  '┗(▔, ▔ )┛',
  '( ͡° ͜ʖ ͡°)',
  '(ง\'̀-\'́)ง',
  '(¬‿¬)',
  '|ω•´)',
  '[uumami]',
  '|ｴ|',
  '◢◣ ◥◤',
  '{ wired }',
]
const spriteIdx = ref(0)
const currentSprite = computed(() => spriteFrames[spriteIdx.value])
let spriteTimer = null

// ========================================
// ticker
// ========================================
const tickerItems = [
  'uumami',
  'present time. present day.',
  'beat entropy',
  'wired',
  'longevity via omics',
  'p vs np (someday)',
  'itam · dacc',
  'nakamas > enemies',
  'frieren says hi',
  'vinlandia online',
  'mhar on gpu',
  'lain loves you',
  'at field stable',
  'host online',
  '2026',
  'data is the new oil. uumami is the new refinery.',
  'no truisms, just what i think',
]
const tickerLoop = [...tickerItems, ...tickerItems] // duplicate for seamless loop

// ========================================
// ambient glyphs
// ========================================
const glyphChars = '人線繋鏡夢永無心時空#∞◊◈◉◎ンル'.split('')
const glyphs = ref([])
let glyphTimer = null

function spawnGlyph() {
  const id = Math.random().toString(36).slice(2)
  const char = glyphChars[Math.floor(Math.random() * glyphChars.length)]
  const side = Math.random() > 0.5 ? 'left' : 'right'
  const top = 10 + Math.random() * 70
  const drift = (Math.random() - 0.5) * 20
  const delay = Math.random() * 1.5
  const duration = 8 + Math.random() * 6
  const opacity = 0.12 + Math.random() * 0.22
  const size = 0.9 + Math.random() * 1.4
  const style = {
    top: `${top}%`,
    [side]: `${5 + Math.random() * 15}%`,
    '--drift': `${drift}px`,
    '--duration': `${duration}s`,
    '--delay': `${delay}s`,
    opacity,
    fontSize: `${size}rem`,
  }
  glyphs.value.push({ id, char, style })
  setTimeout(() => {
    glyphs.value = glyphs.value.filter(g => g.id !== id)
  }, (duration + delay) * 1000)
}

// ========================================
// random glitch flash
// ========================================
const glitching = ref(false)
let glitchTimer = null
function triggerGlitch() {
  glitching.value = true
  setTimeout(() => { glitching.value = false }, 120)
  glitchTimer = setTimeout(triggerGlitch, 6000 + Math.random() * 14000)
}

// ========================================
// lifecycle
// ========================================
onMounted(() => {
  tickClock()
  clockTimer = setInterval(tickClock, 1000)
  spriteTimer = setInterval(() => {
    spriteIdx.value = (spriteIdx.value + 1) % spriteFrames.length
  }, 1800)
  glyphTimer = setInterval(spawnGlyph, 1500)
  for (let i = 0; i < 4; i++) setTimeout(spawnGlyph, i * 600)
  glitchTimer = setTimeout(triggerGlitch, 3000)
})

onUnmounted(() => {
  if (clockTimer) clearInterval(clockTimer)
  if (spriteTimer) clearInterval(spriteTimer)
  if (glyphTimer) clearInterval(glyphTimer)
  if (glitchTimer) clearTimeout(glitchTimer)
})
</script>

<style scoped>
.global-ui {
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 40;
  font-family: 'IBM Plex Mono', ui-monospace, monospace;
}

/* ==== session clock top-right ==== */
.session {
  position: absolute;
  top: 0.7rem; right: 0.9rem;
  font-size: 0.7rem;
  color: #7fffb5;
  display: flex; align-items: center; gap: 0.45rem;
  letter-spacing: 0.1em;
  opacity: 0.82;
  text-transform: uppercase;
  mix-blend-mode: screen;
}
.dot-live {
  width: 6px; height: 6px; border-radius: 999px;
  background: #7fffb5;
  box-shadow: 0 0 10px #7fffb5;
  animation: pulse 1.4s ease-in-out infinite;
}
@keyframes pulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.35; transform: scale(0.7); }
}
.session .sep { opacity: 0.35; }

/* ==== ASCII sprite bottom-right ==== */
.sprite {
  position: absolute;
  bottom: 2rem; right: 1.2rem;
  font-size: 0.9rem;
  color: #7fffb5;
  opacity: 0.75;
  letter-spacing: 0.02em;
  font-weight: 500;
  text-shadow: 0 0 10px rgba(127,255,181,0.45);
  animation: spriteBreath 2s ease-in-out infinite;
  mix-blend-mode: screen;
}
@keyframes spriteBreath {
  0%, 100% { opacity: 0.65; transform: translateY(0); }
  50% { opacity: 0.92; transform: translateY(-1px); }
}

/* ==== bottom ticker ==== */
.ticker {
  position: absolute;
  bottom: 0; left: 0; right: 0;
  height: 1.3rem;
  overflow: hidden;
  background: rgba(11, 15, 13, 0.55);
  border-top: 1px solid rgba(127, 255, 181, 0.18);
}
.ticker-track {
  display: inline-flex;
  white-space: nowrap;
  animation: tickerScroll 90s linear infinite;
  will-change: transform;
}
.ticker-track .item {
  display: inline-flex; align-items: center; gap: 0.5rem;
  padding: 0 0.9rem;
  font-size: 0.72rem;
  color: #7fffb5;
  opacity: 0.72;
  letter-spacing: 0.08em;
  line-height: 1.3rem;
}
.ticker-track .item .sep { opacity: 0.35; color: #2ef5ff; }
@keyframes tickerScroll {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

/* ==== ambient drifting glyphs ==== */
.ambient {
  position: absolute; inset: 0;
  pointer-events: none;
  overflow: hidden;
}
.glyph {
  position: absolute;
  color: #7fffb5;
  font-family: 'Shippori Mincho', 'Noto Serif JP', serif;
  mix-blend-mode: screen;
  animation: drift var(--duration) ease-in-out var(--delay) forwards;
  will-change: transform, opacity;
}
@keyframes drift {
  0%   { transform: translate(0, 20px); opacity: 0; }
  10%  { opacity: var(--_op, 0.25); }
  100% { transform: translate(var(--drift), -80px); opacity: 0; }
}

/* ==== random horizontal glitch flash ==== */
.glitch {
  position: absolute;
  left: 0; right: 0;
  top: 37%;
  height: 3px;
  background: linear-gradient(90deg,
    transparent,
    rgba(46, 245, 255, 0.85) 30%,
    rgba(255, 46, 195, 0.85) 70%,
    transparent);
  opacity: 0;
  transform: scaleY(0);
  pointer-events: none;
  mix-blend-mode: screen;
  filter: blur(1px);
}
.glitch.active {
  animation: glitchFlash 0.12s ease-out;
}
@keyframes glitchFlash {
  0%   { transform: scaleY(0) translateX(0); opacity: 0; }
  20%  { transform: scaleY(6) translateX(-12px); opacity: 1; }
  50%  { transform: scaleY(2) translateX(8px); opacity: 0.85; }
  100% { transform: scaleY(0) translateX(0); opacity: 0; }
}
</style>
