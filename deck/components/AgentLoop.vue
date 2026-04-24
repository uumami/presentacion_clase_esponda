<template>
  <div class="agent">
    <div class="hud">
      <div class="task-input">
        <span class="label">task ›</span>
        <input v-model="task" type="text" :disabled="running" />
      </div>
      <button @click="running ? stop() : start()" :class="{ stop: running }">
        {{ running ? 'stop' : 'run agent' }}
      </button>
      <button @click="reset" :disabled="running">reset</button>
    </div>

    <div class="loop">
      <div
        v-for="(phase, i) in phases"
        :key="i"
        class="phase"
        :class="{ active: currentPhase === i, done: i < currentPhase }"
      >
        <div class="phase-name">{{ phase.name }}</div>
        <div class="phase-sub">{{ phase.sub }}</div>
      </div>
      <div class="arrow" />
    </div>

    <div class="console" ref="consoleRef">
      <div v-for="(line, i) in log" :key="i" class="line" :class="line.kind">
        <span class="t">{{ line.t }}</span>
        <span class="msg">{{ line.msg }}</span>
      </div>
      <div v-if="running" class="line running">
        <span class="t">··</span>
        <span class="msg">
          <span class="blink">▊</span>
        </span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onUnmounted, nextTick } from 'vue'

const phases = [
  { name: 'plan', sub: 'decide qué hacer' },
  { name: 'act', sub: 'llama una tool' },
  { name: 'observe', sub: 'lee el resultado' },
  { name: 'repeat', sub: 'sigue o termina' },
]

const task = ref('averigua el clima en cdmx y agéndame café a las 4pm')
const log = ref([])
const currentPhase = ref(-1)
const running = ref(false)
const consoleRef = ref(null)
let abortFlag = false

const scriptedSteps = [
  { phase: 0, kind: 'think', msg: 'descompongo la tarea: (1) clima cdmx, (2) crear evento 4pm' },
  { phase: 1, kind: 'tool', msg: 'tool call › weather.get(location="cdmx")' },
  { phase: 2, kind: 'result', msg: '← 22°C · parcialmente nublado · humedad 58%' },
  { phase: 3, kind: 'think', msg: 'clima ok, paso a agenda' },
  { phase: 0, kind: 'think', msg: 'planifico evento de café a las 16:00' },
  { phase: 1, kind: 'tool', msg: 'tool call › calendar.create(title="café", time="16:00")' },
  { phase: 2, kind: 'result', msg: '← evento #a7f3 creado' },
  { phase: 3, kind: 'done', msg: 'listo. clima reportado, evento agendado.' },
]

function pushLog(l) {
  const t = new Date().toLocaleTimeString('es-MX', { hour12: false })
  log.value.push({ ...l, t })
  nextTick(() => {
    if (consoleRef.value) consoleRef.value.scrollTop = consoleRef.value.scrollHeight
  })
}

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms))
}

async function start() {
  if (running.value) return
  running.value = true
  abortFlag = false
  log.value = []
  currentPhase.value = -1
  pushLog({ kind: 'user', msg: `› ${task.value}` })
  await sleep(500)
  for (const step of scriptedSteps) {
    if (abortFlag) break
    currentPhase.value = step.phase
    await sleep(650)
    if (abortFlag) break
    pushLog({ kind: step.kind, msg: step.msg })
    await sleep(350)
  }
  if (!abortFlag) {
    currentPhase.value = 3
  }
  running.value = false
}

function stop() {
  abortFlag = true
  running.value = false
  pushLog({ kind: 'warn', msg: 'abort. agent stopped.' })
}

function reset() {
  running.value = false
  abortFlag = true
  log.value = []
  currentPhase.value = -1
}

onUnmounted(() => { abortFlag = true })
</script>

<style scoped>
.agent {
  font-family: var(--font-mono);
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 0.7rem;
}
.hud {
  display: flex;
  gap: 0.5rem;
  align-items: center;
}
.task-input {
  flex: 1;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(255, 58, 47, 0.3);
  border-radius: 4px;
  padding: 0.25rem 0.6rem;
}
.task-input .label {
  color: var(--eva-fg);
  font-size: 0.8rem;
  font-weight: 500;
}
.task-input input {
  flex: 1;
  background: transparent;
  border: 0;
  outline: 0;
  color: var(--eva-ink);
  font-family: var(--font-mono);
  font-size: 0.85rem;
  padding: 0.3rem 0;
}
.hud button {
  background: transparent;
  color: var(--eva-fg);
  border: 1px solid var(--eva-fg);
  border-radius: 3px;
  padding: 0.25rem 0.7rem;
  font-family: var(--font-mono);
  font-size: 0.75rem;
  cursor: pointer;
  text-transform: lowercase;
}
.hud button:hover { background: var(--eva-fg); color: var(--eva-bg); }
.hud button:disabled { opacity: 0.4; cursor: not-allowed; }
.hud button.stop {
  color: var(--cyber-red);
  border-color: var(--cyber-red);
}
.hud button.stop:hover { background: var(--cyber-red); color: var(--eva-bg); }
.loop {
  position: relative;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0.4rem;
}
.phase {
  padding: 0.5rem 0.7rem;
  border: 1px solid rgba(255, 58, 47, 0.25);
  border-radius: 4px;
  background: rgba(10, 5, 17, 0.5);
  transition: all 0.25s;
}
.phase-name {
  color: var(--eva-fg);
  font-size: 0.95rem;
  font-weight: 500;
  letter-spacing: 0.04em;
  text-transform: lowercase;
}
.phase-sub {
  font-size: 0.7rem;
  color: var(--eva-ink);
  opacity: 0.6;
  margin-top: 0.15rem;
}
.phase.done {
  border-color: var(--eva-amber);
  opacity: 0.85;
}
.phase.done .phase-name { color: var(--eva-amber); }
.phase.active {
  border-color: var(--cyber-red);
  background: rgba(255, 0, 68, 0.12);
  box-shadow: 0 0 20px rgba(255, 0, 68, 0.3);
}
.phase.active .phase-name { color: var(--cyber-red); }
.console {
  height: 170px;
  overflow-y: auto;
  background: rgba(0, 0, 0, 0.45);
  border: 1px solid rgba(255, 58, 47, 0.2);
  border-radius: 4px;
  padding: 0.5rem 0.7rem;
  font-size: 0.78rem;
  line-height: 1.4;
  display: flex;
  flex-direction: column;
  gap: 0.1rem;
}
.line {
  display: flex;
  gap: 0.5rem;
}
.line .t {
  color: var(--eva-amber);
  opacity: 0.55;
  min-width: 3.8rem;
  font-size: 0.7rem;
}
.line .msg { color: var(--eva-ink); opacity: 0.92; }
.line.user .msg { color: var(--eva-amber); font-weight: 500; }
.line.think .msg { color: var(--eva-ink); opacity: 0.75; font-style: italic; }
.line.tool .msg { color: var(--cyber-cyan); }
.line.result .msg { color: var(--lain-fg); }
.line.done .msg { color: var(--eva-fg); font-weight: 500; }
.line.warn .msg { color: var(--cyber-red); }
.blink { animation: bl 1s steps(1) infinite; color: var(--eva-fg); }
@keyframes bl {
  0%, 49% { opacity: 1; }
  50%, 100% { opacity: 0; }
}
</style>
