<template>
  <span class="slashes">
    <template v-for="(item, i) in items" :key="i">
      <span class="item">{{ item }}</span>
      <span v-if="i < items.length - 1" class="sep">/</span>
    </template>
  </span>
</template>

<script setup>
defineProps({
  items: { type: Array, required: true },
});
</script>

<style scoped>
.slashes {
  font-family: var(--font-mono);
  font-size: 1rem;
  letter-spacing: 0.08em;
  opacity: 0.8;
}
.sep {
  margin: 0 0.45em;
  opacity: 0.35;
}
</style>
