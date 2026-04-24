<template>
  <div class="crt-wrap" :class="{ scanlines }">
    <slot />
    <div v-if="glitch" class="glitch-overlay" />
  </div>
</template>

<script setup>
defineProps({
  scanlines: { type: Boolean, default: true },
  glitch: { type: Boolean, default: false },
});
</script>

<style scoped>
.crt-wrap {
  position: relative;
  width: 100%;
  height: 100%;
}
.crt-wrap.scanlines::before {
  content: '';
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(
    0deg,
    rgba(0, 0, 0, 0.22) 0px,
    rgba(0, 0, 0, 0.22) 1px,
    transparent 1px,
    transparent 3px
  );
  pointer-events: none;
  z-index: 50;
  mix-blend-mode: multiply;
}
.glitch-overlay {
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 51;
  background: linear-gradient(
    90deg,
    transparent 0%,
    rgba(46, 245, 255, 0.03) 40%,
    rgba(255, 46, 195, 0.03) 60%,
    transparent 100%
  );
  animation: flicker 4s infinite;
}
@keyframes flicker {
  0%, 100% { opacity: 0.6; }
  45% { opacity: 0.95; }
  47% { opacity: 0.3; }
  49% { opacity: 0.85; }
}
</style>
