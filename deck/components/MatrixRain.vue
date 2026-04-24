<template>
  <canvas ref="canvasRef" class="matrix-rain" />
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const props = defineProps({
  color: { type: String, default: 'rgba(127, 255, 181, 0.85)' },
  fade: { type: String, default: 'rgba(11, 15, 13, 0.06)' },
  fontSize: { type: Number, default: 18 },
  density: { type: Number, default: 0.975 },
})

const canvasRef = ref(null)
const chars = (
  'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲンンン'
  + '0123456789'
  + 'uumamilainwiredpresentday'
).split('')

let raf = null
let ctx = null
let drops = []
let cols = 0

function setup() {
  const canvas = canvasRef.value
  if (!canvas) return
  canvas.width = canvas.offsetWidth
  canvas.height = canvas.offsetHeight
  ctx = canvas.getContext('2d')
  cols = Math.floor(canvas.width / props.fontSize)
  drops = new Array(cols).fill(0).map(() => Math.random() * canvas.height / props.fontSize)
}

function draw() {
  const canvas = canvasRef.value
  if (!canvas || !ctx) return
  ctx.fillStyle = props.fade
  ctx.fillRect(0, 0, canvas.width, canvas.height)
  ctx.font = `${props.fontSize}px "IBM Plex Mono", ui-monospace, monospace`
  for (let i = 0; i < cols; i++) {
    const t = chars[Math.floor(Math.random() * chars.length)]
    const y = drops[i] * props.fontSize
    const head = Math.random() > 0.96
    ctx.fillStyle = head ? '#e8fff3' : props.color
    ctx.fillText(t, i * props.fontSize, y)
    if (y > canvas.height && Math.random() > props.density) drops[i] = 0
    drops[i]++
  }
  raf = requestAnimationFrame(draw)
}

function init() {
  setup()
  if (raf) cancelAnimationFrame(raf)
  draw()
}

onMounted(() => {
  init()
  window.addEventListener('resize', init)
})
onUnmounted(() => {
  if (raf) cancelAnimationFrame(raf)
  window.removeEventListener('resize', init)
})
</script>

<style scoped>
.matrix-rain {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}
</style>
