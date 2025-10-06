<template>
  <button :class="buttonClasses" :disabled="disabled" @click="handleClick"></button>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps({
  variant: {
    type: String,
    default: 'primary',
    validator: (v: unknown) => ['primary', 'secondary', 'danger'].includes(v as string),
  },
  size: {
    type: String,
    default: 'md',
  },
  disabled: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits(['click'])

const buttonClasses = computed(() => [
  'btn',
  `btn-${props.variant}`,
  `btn-${props.size}`,
  { 'btn-disabled': props.disabled },
])

const handleClick = (e: MouseEvent) => {
  if (!props.disabled) {
    emit('click', e)
  }
}
</script>

<style scoped>
.btn {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.2s;
}

.btn-primary {
  background: #3b82f6;
  color: white;
}

.btn-primary:hover {
  background: #2563eb;
}

.btn-secondary {
  background: #6b7280;
  color: white;
}

.btn-danger {
  background: #ef4444;
  color: white;
}

.btn-sm {
  padding: 0.25rem 0.75rem;
  font-size: 0.875rem;
}
.btn-md {
  padding: 0.5rem 1rem;
}
.btn-lg {
  padding: 0.75rem 1.5rem;
  font-size: 1.125rem;
}

.btn-disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
</style>
