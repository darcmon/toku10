<script setup lang="ts">
import { computed } from 'vue'
import type { TeamGameStats } from '../../types/api'

const props = defineProps<{
  awayStats: TeamGameStats
  homeStats: TeamGameStats
}>()

interface CompareRow {
  label: string
  away: string
  home: string
  awayShare: number // 0-100, away side's proportion of the bar
  leader: 'away' | 'home' | null
}

function pct(made: number | null, att: number | null): number | null {
  if (!att) return null
  return ((made ?? 0) / att) * 100
}

function fmtPct(v: number | null): string {
  return v === null ? '–' : `${v.toFixed(1)}%`
}

const rows = computed<CompareRow[]>(() => {
  const a = props.awayStats
  const h = props.homeStats
  const out: CompareRow[] = []

  const push = (label: string, av: number | null, hv: number | null, fmt: (v: number | null) => string, lowerWins = false) => {
    if (av === null && hv === null) return
    const aw = av ?? 0
    const hw = hv ?? 0
    const leader = aw === hw ? null : (aw > hw) !== lowerWins ? 'away' : 'home'
    out.push({
      label,
      away: fmt(av),
      home: fmt(hv),
      awayShare: aw + hw === 0 ? 50 : Math.round((aw / (aw + hw)) * 100),
      leader,
    })
  }

  const raw = (v: number | null) => (v === null ? '–' : String(v))
  push('Field goals', pct(a.field_goals_made, a.field_goals_attempted), pct(h.field_goals_made, h.field_goals_attempted), fmtPct)
  push('Three pointers', pct(a.three_pointers_made, a.three_pointers_attempted), pct(h.three_pointers_made, h.three_pointers_attempted), fmtPct)
  push('Free throws', pct(a.free_throws_made, a.free_throws_attempted), pct(h.free_throws_made, h.free_throws_attempted), fmtPct)
  push('Rebounds', a.rebounds, h.rebounds, raw)
  push('Assists', a.assists, h.assists, raw)
  push('Turnovers', a.turnovers, h.turnovers, raw, true)
  return out
})
</script>

<template>
  <div class="grid grid-cols-1 gap-x-6 gap-y-2.5 border-t-[0.5px] border-hairline px-6 py-4 sm:grid-cols-2 lg:grid-cols-3">
    <div v-for="row in rows" :key="row.label">
      <div class="mb-1 flex justify-between text-xs">
        <span class="font-mono text-ink">{{ row.away }}</span>
        <span class="text-[11px] text-ink-faint">{{ row.label }}</span>
        <span class="font-mono text-ink-dim">{{ row.home }}</span>
      </div>
      <div class="flex h-1 gap-0.5">
        <div
          class="rounded-sm"
          :class="row.leader === 'away' ? 'bg-accent-400' : 'bg-hairline'"
          :style="{ width: row.awayShare + '%' }"
        ></div>
        <div
          class="flex-1 rounded-sm"
          :class="row.leader === 'home' ? 'bg-accent-400' : 'bg-hairline'"
        ></div>
      </div>
    </div>
  </div>
</template>
