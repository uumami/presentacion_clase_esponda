<template>
  <div class="rag">
    <form class="rag-input" @submit.prevent="search">
      <span class="prompt">query ›</span>
      <input
        ref="inputRef"
        v-model="query"
        type="text"
        placeholder="prueba: polytope · chatbot · lain · nestlé"
        autocomplete="off"
      />
      <button type="submit">retrieve</button>
    </form>

    <div class="corpus">
      <div
        v-for="c in scored"
        :key="c.id"
        class="chunk"
        :class="{ hit: c.rank !== null, top: c.rank === 0 }"
        :style="{ '--score': c.score }"
      >
        <div class="meta">
          <span class="cid">#{{ c.id.toString().padStart(2, '0') }}</span>
          <span v-if="c.rank !== null" class="rank">top-{{ c.rank + 1 }}</span>
          <span v-if="query" class="score">{{ c.score.toFixed(2) }}</span>
        </div>
        <div class="text">{{ c.text }}</div>
      </div>
    </div>

    <div class="status">
      <span v-if="!query" class="hint">escribe una query y mira la similitud sobre {{ corpus.length }} chunks</span>
      <span v-else class="hint">top-{{ k }} con mayor similitud jaccard · los demás quedan fuera del contexto</span>
    </div>
  </div>
</template>

<script setup>
import { computed, ref, onMounted } from 'vue'

const k = 3

const corpus = [
  { id: 1, text: 'mhar samplea puntos uniformes en polítopos usando matriz por matriz en gpu.' },
  { id: 2, text: 'lain. present time, present day. close the world. open the next.' },
  { id: 3, text: 'un chatbot combina asr, nlu, rag, llm, guardrails y tts.' },
  { id: 4, text: 'rag mete documentos relevantes al contexto del llm antes de generar.' },
  { id: 5, text: 'maira de nestlé detecta malnutrición por foto, patente en trámite.' },
  { id: 6, text: 'agentes autónomos hacen tool use y loops: plan, act, observe, repeat.' },
  { id: 7, text: 'mhar paper · arxiv 2104.07097 · springer computational statistics 2023.' },
  { id: 8, text: 'suggestic construye chatbots de salud con voz y texto conversacional.' },
  { id: 9, text: 'frieren es una maga que viaja por mil años después de matar al demon king.' },
  { id: 10, text: 'ghost in the shell explora qué significa ser consciencia en un mundo con redes.' },
  { id: 11, text: 'evangelion usa la cruz como símbolo de at field, no como religión directa.' },
  { id: 12, text: 'causalidad no es correlación · do-operator mide la intervención directa.' },
  { id: 13, text: 'tycoon points es mi proyecto quant · backtests y options chains.' },
  { id: 14, text: 'cura ganó hult prize 2026 · asistente para cuidadores de demencia.' },
]

const query = ref('')
const inputRef = ref(null)

function tokenize(s) {
  return new Set(
    s.toLowerCase()
      .replace(/[^\w\sáéíóúñ]/g, ' ')
      .split(/\s+/)
      .filter(w => w.length >= 3),
  )
}

function jaccard(a, b) {
  if (a.size === 0 || b.size === 0) return 0
  let inter = 0
  for (const x of a) if (b.has(x)) inter++
  const uni = a.size + b.size - inter
  return inter / uni
}

const scored = computed(() => {
  if (!query.value.trim()) {
    return corpus.map(c => ({ ...c, score: 0, rank: null }))
  }
  const qt = tokenize(query.value)
  const withScore = corpus.map(c => ({
    ...c,
    score: jaccard(qt, tokenize(c.text)),
  }))
  const top = [...withScore]
    .filter(c => c.score > 0)
    .sort((a, b) => b.score - a.score)
    .slice(0, k)
  const topIds = top.map(c => c.id)
  return withScore.map(c => ({
    ...c,
    rank: topIds.includes(c.id) ? topIds.indexOf(c.id) : null,
  }))
})

function search() {
  // noop, computed already reacts
}

onMounted(() => { if (inputRef.value) inputRef.value.focus() })
</script>

<style scoped>
.rag {
  font-family: var(--font-mono);
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}
.rag-input {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(127, 255, 181, 0.25);
  border-radius: 4px;
  padding: 0.3rem 0.7rem;
}
.rag-input .prompt {
  color: var(--lain-fg);
  font-weight: 500;
  font-size: 0.85rem;
}
.rag-input input {
  flex: 1;
  background: transparent;
  border: 0;
  outline: 0;
  color: var(--lain-ink);
  font-family: var(--font-mono);
  font-size: 0.9rem;
  padding: 0.3rem 0;
}
.rag-input button {
  background: transparent;
  color: var(--lain-fg);
  border: 1px solid var(--lain-fg);
  border-radius: 3px;
  padding: 0.2rem 0.6rem;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  cursor: pointer;
  text-transform: lowercase;
}
.rag-input button:hover {
  background: var(--lain-fg);
  color: var(--lain-bg);
}
.corpus {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.35rem 0.5rem;
  max-height: 220px;
  overflow-y: auto;
  padding-right: 0.3rem;
}
.chunk {
  display: flex;
  flex-direction: column;
  gap: 0.15rem;
  padding: 0.35rem 0.5rem;
  border: 1px solid rgba(127, 255, 181, 0.12);
  border-radius: 3px;
  opacity: 0.35;
  transition: all 0.2s;
  background: rgba(0, 0, 0, 0.22);
}
.chunk.hit {
  opacity: 1;
  border-color: var(--vapor-cyan);
  background: rgba(46, 245, 255, 0.08);
  box-shadow: 0 0 12px rgba(46, 245, 255, 0.2);
}
.chunk.top {
  border-color: var(--lain-fg);
  background: rgba(127, 255, 181, 0.14);
  box-shadow: 0 0 20px rgba(127, 255, 181, 0.3);
}
.meta {
  display: flex;
  gap: 0.4rem;
  align-items: baseline;
  font-size: 0.7rem;
}
.cid { color: var(--vapor-mag); font-weight: 500; }
.rank {
  color: var(--lain-fg);
  font-weight: 600;
  letter-spacing: 0.05em;
  text-transform: lowercase;
}
.score { color: var(--vapor-cyan); opacity: 0.7; }
.chunk .text {
  font-size: 0.72rem;
  line-height: 1.35;
  color: var(--lain-ink);
}
.status {
  font-size: 0.75rem;
  opacity: 0.7;
  padding-top: 0.1rem;
}
.hint { color: var(--vapor-cyan); }
</style>
