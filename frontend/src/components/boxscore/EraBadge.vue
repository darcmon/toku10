<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{
  name: string
  rarity: number
}>()

// DESIGN.md rule 3: legendary badges are dark chips even on light surfaces;
// lower tiers stay quiet light pills.
const isLegendary = computed(() => props.rarity >= 5)

const tier = computed(() => {
  if (props.rarity >= 5) return 'legendary'
  if (props.rarity >= 4) return 'epic'
  if (props.rarity >= 2) return 'rare'
  return 'common'
})

const pillClasses: Record<string, string> = {
  epic: 'bg-epic-100 text-epic-800',
  rare: 'bg-rare-100 text-rare-800',
  common: 'bg-common-100 text-common-800',
}
</script>

<template>
  <span
    v-if="isLegendary"
    class="inline-block rounded-[3px] border border-legendary-600 bg-legendary-900 px-2 py-0.5 align-[1px] text-[10px] font-medium tracking-widest whitespace-nowrap text-legendary-300 uppercase"
  >
    {{ name }}
  </span>
  <span
    v-else
    class="inline-block rounded-full px-2 py-0.5 align-[1px] text-[10px] font-medium whitespace-nowrap"
    :class="pillClasses[tier]"
  >
    {{ name }}
  </span>
</template>
