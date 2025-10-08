<script setup lang="ts">
import { useCounterStore } from '../stores/counter'
const counter = useCounterStore()
</script>

<template>
  <div>
    <h2>Counter</h2>
    <p>Count: {{ counter.count }}</p>
    <p>Double: {{ counter.doubleCount }}</p>
    <button @click="counter.increment">Increment</button>
  </div>
</template>

<style scoped>
button {
  margin-top: 8px;
}
</style>
