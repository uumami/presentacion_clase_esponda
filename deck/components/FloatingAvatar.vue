<template>
  <img
    class="avatar-floating"
    :class="size"
    :src="src"
    :alt="alt"
  />
</template>

<script setup>
defineProps({
  src: { type: String, required: true },
  alt: { type: String, default: 'uumami' },
  size: { type: String, default: 'md' },
});
</script>

<style scoped>
.avatar-floating {
  position: absolute;
  right: 2.5rem;
  bottom: 2.5rem;
  border-radius: 999px;
  object-fit: cover;
  border: 2px solid rgba(255, 255, 255, 0.18);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.55);
  z-index: 20;
}
.sm { width: 120px; height: 120px; }
.md { width: 180px; height: 180px; }
.lg { width: 260px; height: 260px; }
</style>
