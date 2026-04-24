<template>
  <div class="chatbot">
    <div class="chat-body" ref="bodyRef">
      <div v-for="(m, i) in messages" :key="i" class="msg" :class="m.role">
        <span class="who">{{ m.role === 'user' ? 'tú' : 'bot' }}</span>
        <span class="text">{{ m.text }}</span>
      </div>
      <div v-if="typing" class="msg bot typing">
        <span class="who">bot</span>
        <span class="text">
          <span class="dot" />
          <span class="dot" />
          <span class="dot" />
        </span>
      </div>
    </div>
    <form class="chat-input" @submit.prevent="send">
      <span class="prompt">›</span>
      <input
        ref="inputRef"
        v-model="draft"
        type="text"
        placeholder="prueba: hola · rag · agente · chatbot"
        autocomplete="off"
      />
      <button type="submit">send</button>
    </form>
    <div class="suggestions">
      <button
        v-for="s in suggestions"
        :key="s"
        type="button"
        class="chip"
        @click="quick(s)"
      >
        {{ s }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, nextTick, onMounted } from 'vue'

const suggestions = ['hola', 'rag', 'agente', 'chatbot', 'profe', 'longevidad']

const responses = {
  hola: 'present time, present day.',
  hi: 'present time, present day.',
  rag: 'retrieval-augmented generation. busco los chunks correctos antes de responder.',
  agente: 'tool use + loops. plan → act → observe → repeat. yo no solo respondo, actúo.',
  agent: 'tool use + loops. plan → act → observe → repeat.',
  chatbot: 'soy uno. asr → nlu → rag → llm → guardrails → tts.',
  profe: 'inteligencia artificial · fuentes de datos · chatbots/automl · itam · 4.74',
  longevidad: 'simular organismos con omics + ia. beat entropy.',
  mhar: 'sampleador de polítopos más rápido del mundo. matrix × matrix en gpu.',
  cura: 'cto + cso. hult prize 2026. asistente para cuidadores.',
  lain: 'no matter where you go, everyone is connected.',
  help: 'prueba: hola, rag, agente, chatbot, profe, longevidad, mhar, cura, lain',
  default: 'no tengo guión para eso. prueba "help".',
}

const messages = ref([
  { role: 'bot', text: 'soy un bot scripted. prueba algo.' },
])
const draft = ref('')
const typing = ref(false)
const bodyRef = ref(null)
const inputRef = ref(null)

function lookup(q) {
  const k = q.trim().toLowerCase()
  for (const key of Object.keys(responses)) {
    if (key !== 'default' && k.includes(key))
      return responses[key]
  }
  return responses.default
}

async function scrollDown() {
  await nextTick()
  if (bodyRef.value) bodyRef.value.scrollTop = bodyRef.value.scrollHeight
}

async function send() {
  const q = draft.value.trim()
  if (!q) return
  messages.value.push({ role: 'user', text: q })
  draft.value = ''
  await scrollDown()
  typing.value = true
  await new Promise(r => setTimeout(r, 600 + Math.random() * 400))
  typing.value = false
  messages.value.push({ role: 'bot', text: lookup(q) })
  await scrollDown()
}

async function quick(s) {
  draft.value = s
  await send()
}

onMounted(() => { if (inputRef.value) inputRef.value.focus() })
</script>

<style scoped>
.chatbot {
  font-family: var(--font-mono);
  width: 100%;
  max-width: 640px;
  background: rgba(10, 20, 16, 0.6);
  border: 1px solid rgba(127, 255, 181, 0.25);
  border-radius: 6px;
  padding: 0.9rem;
  display: flex;
  flex-direction: column;
  gap: 0.7rem;
}
.chat-body {
  height: 240px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
  padding: 0.5rem;
  background: rgba(0, 0, 0, 0.3);
  border-radius: 4px;
  font-size: 0.85rem;
}
.msg {
  display: flex;
  gap: 0.5rem;
  line-height: 1.35;
}
.msg .who {
  color: var(--vapor-cyan);
  font-weight: 500;
  min-width: 2rem;
  opacity: 0.7;
}
.msg.user .who { color: var(--vapor-mag); }
.msg .text { color: var(--lain-ink); }
.msg.bot .text { color: var(--lain-fg); }
.chat-input {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(127, 255, 181, 0.18);
  border-radius: 4px;
  padding: 0.25rem 0.6rem;
}
.chat-input .prompt {
  color: var(--lain-fg);
  font-weight: 500;
}
.chat-input input {
  flex: 1;
  background: transparent;
  border: 0;
  outline: 0;
  color: var(--lain-ink);
  font-family: var(--font-mono);
  font-size: 0.9rem;
  padding: 0.3rem 0;
}
.chat-input button {
  background: transparent;
  color: var(--lain-fg);
  border: 1px solid var(--lain-fg);
  border-radius: 3px;
  padding: 0.2rem 0.6rem;
  font-family: var(--font-mono);
  font-size: 0.75rem;
  cursor: pointer;
  text-transform: lowercase;
}
.chat-input button:hover {
  background: var(--lain-fg);
  color: var(--lain-bg);
}
.suggestions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.3rem;
}
.suggestions .chip {
  background: transparent;
  color: var(--lain-ink);
  border: 1px solid rgba(127, 255, 181, 0.3);
  border-radius: 999px;
  padding: 0.18rem 0.6rem;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  cursor: pointer;
  opacity: 0.8;
  text-transform: lowercase;
}
.suggestions .chip:hover {
  background: rgba(127, 255, 181, 0.1);
  opacity: 1;
}
.typing .text { display: inline-flex; gap: 0.15rem; align-items: center; padding-top: 0.2rem; }
.typing .dot {
  width: 4px; height: 4px; border-radius: 999px;
  background: var(--lain-fg);
  animation: tp 1s infinite;
}
.typing .dot:nth-child(2) { animation-delay: 0.15s; }
.typing .dot:nth-child(3) { animation-delay: 0.3s; }
@keyframes tp {
  0%, 60%, 100% { opacity: 0.2; }
  30% { opacity: 1; }
}
</style>
