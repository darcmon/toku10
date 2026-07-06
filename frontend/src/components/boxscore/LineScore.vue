<script setup lang="ts">
import { computed } from 'vue'
import type { TeamGameStats } from '../../types/api'

const props = defineProps<{
  awayAbbr: string
  homeAbbr: string
  awayStats: TeamGameStats
  homeStats: TeamGameStats
}>()

const periods = computed(() => {
  const n = Math.max(props.awayStats.quarter_scores.length, props.homeStats.quarter_scores.length)
  return Array.from({ length: n }, (_, i) => (i < 4 ? `Q${i + 1}` : `OT${i - 3 > 1 ? i - 3 : ''}`))
})

const awayTotal = computed(() => props.awayStats.points ?? 0)
const homeTotal = computed(() => props.homeStats.points ?? 0)
const awayWon = computed(() => awayTotal.value > homeTotal.value)

function isHighQuarter(scores: number[], i: number): boolean {
  return scores[i] === Math.max(...scores)
}
</script>

<template>
  <div class="px-6 pb-4">
    <table class="w-full border-collapse font-mono text-[13px]">
      <tbody>
        <tr class="text-[11px] text-ink-faint">
          <td class="py-1 font-sans"></td>
          <td v-for="p in periods" :key="p" class="px-2 py-1 text-right">{{ p }}</td>
          <td class="py-1 pl-2 text-right font-medium">T</td>
        </tr>
        <tr class="border-t-[0.5px] border-hairline">
          <td class="py-1.5 font-sans text-xs text-ink">{{ awayAbbr }}</td>
          <td
            v-for="(q, i) in awayStats.quarter_scores"
            :key="i"
            class="px-2 py-1.5 text-right"
            :class="awayWon && isHighQuarter(awayStats.quarter_scores, i) ? 'font-medium text-ink' : 'text-ink-dim'"
          >
            {{ q }}
          </td>
          <td class="py-1.5 pl-2 text-right font-medium" :class="awayWon ? 'text-ink' : 'text-ink-faint'">
            {{ awayTotal }}
          </td>
        </tr>
        <tr class="border-t-[0.5px] border-hairline">
          <td class="py-1.5 font-sans text-xs text-ink">{{ homeAbbr }}</td>
          <td
            v-for="(q, i) in homeStats.quarter_scores"
            :key="i"
            class="px-2 py-1.5 text-right"
            :class="!awayWon && isHighQuarter(homeStats.quarter_scores, i) ? 'font-medium text-ink' : 'text-ink-dim'"
          >
            {{ q }}
          </td>
          <td class="py-1.5 pl-2 text-right font-medium" :class="!awayWon ? 'text-ink' : 'text-ink-faint'">
            {{ homeTotal }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
