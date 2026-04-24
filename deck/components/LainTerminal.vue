<template>
  <div class="term">
    <div class="term-bar">
      <span class="dot r" />
      <span class="dot y" />
      <span class="dot g" />
      <span class="path">~/wired</span>
    </div>
    <div class="term-body" ref="bodyRef">
      <div v-for="(line, i) in visible" :key="i" class="line">
        <template v-if="line.type === 'prompt'">
          <span class="user">uumami@wired</span><span class="sep">:</span><span class="cwd">~</span><span class="sign">$</span>
          <span class="cmd">{{ line.text }}</span>
        </template>
        <template v-else-if="line.type === 'out'">
          <span class="out" v-html="line.text" />
        </template>
        <template v-else>
          <span class="blank">&nbsp;</span>
        </template>
      </div>
      <div v-if="typing" class="line">
        <span class="user">uumami@wired</span><span class="sep">:</span><span class="cwd">~</span><span class="sign">$</span>
        <span class="cmd">{{ currentCmd }}<span class="caret">▊</span></span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const script = [
  { type: 'prompt', text: 'whoami' },
  { type: 'out', text: 'uumami // profe / ds / researcher / husbande' },
  { type: 'prompt', text: 'ls projects/' },
  { type: 'out', text: 'lain-shell/   raya-lucaria/   tycoon-points/   peque-llm/' },
  { type: 'prompt', text: 'cat dream.txt' },
  { type: 'out', text: 'beat entropy.  solve p vs np.  longevity for everyone.' },
  { type: 'prompt', text: 'echo $STATUS' },
  { type: 'out', text: 'present time. present day.' },
];

const visible = ref([]);
const typing = ref(false);
const currentCmd = ref('');
const bodyRef = ref(null);
let tickHandle = null;

async function typeLine(text, delay = 45) {
  typing.value = true;
  currentCmd.value = '';
  for (const ch of text) {
    currentCmd.value += ch;
    await wait(delay);
  }
  await wait(300);
  typing.value = false;
}

const wait = (ms) => new Promise((r) => setTimeout(r, ms));

async function run() {
  for (const step of script) {
    if (step.type === 'prompt') {
      await typeLine(step.text);
      visible.value.push(step);
    } else {
      await wait(150);
      visible.value.push(step);
    }
    await wait(350);
    if (bodyRef.value) bodyRef.value.scrollTop = bodyRef.value.scrollHeight;
  }
}

onMounted(() => {
  run();
});
onUnmounted(() => {
  if (tickHandle) clearTimeout(tickHandle);
});
</script>

<style scoped>
.term {
  background: #060907;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.7), 0 0 60px rgba(127, 255, 181, 0.08);
  font-family: var(--font-mono);
  color: var(--lain-fg);
  width: 780px;
  max-width: 100%;
}
.term-bar {
  background: #111;
  padding: 0.6rem 0.9rem;
  display: flex;
  align-items: center;
  gap: 0.4rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}
.dot {
  width: 11px;
  height: 11px;
  border-radius: 999px;
  display: inline-block;
}
.dot.r { background: #ff5f56; }
.dot.y { background: #ffbd2e; }
.dot.g { background: #27c93f; }
.path {
  margin-left: 0.75rem;
  font-size: 0.8rem;
  color: rgba(255, 255, 255, 0.5);
}
.term-body {
  padding: 1rem 1.2rem;
  min-height: 320px;
  max-height: 420px;
  overflow-y: auto;
  font-size: 1rem;
  line-height: 1.55;
  position: relative;
}
.term-body::after {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: repeating-linear-gradient(
    0deg,
    rgba(0, 0, 0, 0.18) 0px,
    rgba(0, 0, 0, 0.18) 1px,
    transparent 1px,
    transparent 3px
  );
  mix-blend-mode: multiply;
}
.line { white-space: pre-wrap; }
.user { color: var(--lain-fg); font-weight: 600; }
.sep { color: rgba(127, 255, 181, 0.4); }
.cwd { color: var(--vapor-cyan); }
.sign { color: rgba(127, 255, 181, 0.6); margin-right: 0.4rem; }
.cmd { color: var(--lain-ink); }
.out { color: rgba(232, 255, 243, 0.8); }
.caret {
  display: inline-block;
  animation: blink 1s steps(1) infinite;
  color: var(--lain-fg);
}
@keyframes blink {
  0%, 49% { opacity: 1; }
  50%, 100% { opacity: 0; }
}
</style>
