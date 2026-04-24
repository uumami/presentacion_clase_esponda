<template>
  <div class="quiz">
    <div class="choices">
      <button
        v-for="(rol, i) in roles"
        :key="i"
        class="rol"
        :class="{ active: selected === i }"
        @click="selected = i"
      >
        <div class="glyph">{{ rol.glyph }}</div>
        <div class="name">{{ rol.name }}</div>
      </button>
    </div>

    <transition name="fade">
      <div v-if="selected !== null" class="panel">
        <div class="panel-name">{{ current.name }}</div>
        <div class="panel-tag">{{ current.tag }}</div>
        <ul class="panel-items">
          <li v-for="b in current.bullets" :key="b">{{ b }}</li>
        </ul>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const roles = [
  {
    glyph: '∑',
    name: 'analyst',
    tag: 'pregunta → dashboard → decisión',
    bullets: [
      'vive en sql, excel/sheets, bi tools',
      'traduce números a decisiones de negocio',
      'puerta de entrada más común al mundo ds',
    ],
  },
  {
    glyph: '⎔',
    name: 'ml engineer',
    tag: 'modelo → api → producción',
    bullets: [
      'convierte notebooks en servicios',
      'docker, apis, latencia, monitoreo',
      'más ingeniería que estadística',
    ],
  },
  {
    glyph: '∞',
    name: 'researcher',
    tag: 'paper → método → experimento',
    bullets: [
      'lee arxiv de desayuno',
      'matemáticas, escritura, experimentos controlados',
      'industria o academia, a veces ambas',
    ],
  },
  {
    glyph: '✦',
    name: 'founder',
    tag: 'problema → producto → dinero',
    bullets: [
      'aprende todo lo necesario para enviar',
      'prioriza distribución sobre tecnología',
      'la mayoría truena, los que no cambian el mundo',
    ],
  },
];

const selected = ref(null);
const current = computed(() => (selected.value !== null ? roles[selected.value] : null));
</script>

<style scoped>
.quiz {
  display: grid;
  grid-template-columns: 1fr 1.2fr;
  gap: 2rem;
  width: 100%;
  max-width: 1100px;
}
.choices {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.75rem;
}
.rol {
  background: transparent;
  color: var(--elden-ink);
  border: 1px solid rgba(201, 161, 89, 0.3);
  padding: 1.25rem;
  border-radius: 6px;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  font-family: var(--font-mono);
  transition: all 0.2s;
}
.rol:hover,
.rol.active {
  border-color: var(--elden-fg);
  background: rgba(201, 161, 89, 0.08);
  box-shadow: 0 0 40px rgba(201, 161, 89, 0.15);
}
.glyph {
  font-family: var(--font-display);
  font-size: 2.5rem;
  color: var(--elden-fg);
  line-height: 1;
}
.name {
  font-size: 1rem;
  letter-spacing: 0.08em;
  text-transform: lowercase;
}
.panel {
  padding: 1.5rem 1.75rem;
  border-left: 2px solid var(--elden-fg);
}
.panel-name {
  font-family: var(--font-display);
  font-size: 2.2rem;
  color: var(--elden-fg);
  text-transform: lowercase;
  letter-spacing: 0.02em;
  margin-bottom: 0.25rem;
}
.panel-tag {
  font-family: var(--font-mono);
  font-size: 0.95rem;
  opacity: 0.7;
  margin-bottom: 1rem;
}
.panel-items {
  list-style: none;
  padding: 0;
  margin: 0;
}
.panel-items li {
  padding: 0.4rem 0;
  font-size: 1.05rem;
  opacity: 0.92;
  border-bottom: 1px dashed rgba(201, 161, 89, 0.2);
}
.fade-enter-active,
.fade-leave-active { transition: opacity 0.25s; }
.fade-enter-from,
.fade-leave-to { opacity: 0; }
</style>
