<template>
  <QrcodeVue
    :value="value"
    :size="Number(size)"
    :level="level"
    :background="background"
    :foreground="foreground"
    :margin="Number(margin)"
  />
</template>

<script setup>
import QrcodeVue from 'qrcode.vue'

defineProps({
  value: { type: String, required: true },
  size: { type: [Number, String], default: 200 },
  level: { type: String, default: 'H' },
  background: { type: String, default: '#0b0f0d' },
  foreground: { type: String, default: '#7fffb5' },
  margin: { type: [Number, String], default: 0 },
})
</script>
