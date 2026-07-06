<script setup lang="ts"></script>

<template>
  <div class="min-h-screen bg-paper-dim">
    <header class="border-b-[0.5px] border-hairline bg-paper">
      <div class="mx-auto flex max-w-3xl items-center justify-between px-4 py-3">
        <router-link to="/" class="text-[15px] font-medium tracking-tight text-ink">notches</router-link>
        <span class="text-xs text-ink-faint">NBA · 2024-25</span>
      </div>
    </header>
    <router-view />
  </div>
</template>
