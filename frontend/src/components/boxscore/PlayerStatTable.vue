<script setup lang="ts">
import type { BoxscorePlayer, CurrentEraResponse, EraDefinition, TeamGameStats } from '../../types/api'
import EraBadge from './EraBadge.vue'

const props = defineProps<{
  teamName: string
  players: BoxscorePlayer[]
  teamStats: TeamGameStats | null
  erasByPlayer: Map<number, CurrentEraResponse>
  eraDefs: Map<number, EraDefinition>
}>()

function shortName(p: BoxscorePlayer): string {
  return `${p.first_name.charAt(0)}. ${p.last_name}`
}

function shots(made: number | null, att: number | null): string {
  if (made === null && att === null) return '–'
  return `${made ?? 0}-${att ?? 0}`
}

function plusMinus(v: number | null): string {
  if (v === null) return '–'
  return v > 0 ? `+${v}` : String(v)
}

function activeEra(playerId: number): { name: string; rarity: number } | null {
  const era = props.erasByPlayer.get(playerId)?.active_era
  if (!era) return null
  const def = props.eraDefs.get(era.era_id)
  return { name: era.era_name, rarity: def?.rarity ?? 1 }
}
</script>

<template>
  <div>
    <p class="mb-2 text-[13px] font-medium text-ink">{{ teamName }}</p>
    <table class="w-full table-fixed border-collapse text-[13px]">
      <thead>
        <tr>
          <th class="py-1 text-left text-[11px] font-normal text-ink-faint">Player</th>
          <th class="w-[34px] py-1 pl-1.5 text-right text-[11px] font-normal text-ink-faint">Min</th>
          <th class="w-[34px] py-1 pl-1.5 text-right text-[11px] font-normal text-ink-faint">Pts</th>
          <th class="w-[34px] py-1 pl-1.5 text-right text-[11px] font-normal text-ink-faint">Reb</th>
          <th class="w-[34px] py-1 pl-1.5 text-right text-[11px] font-normal text-ink-faint">Ast</th>
          <th class="w-[44px] py-1 pl-1.5 text-right text-[11px] font-normal text-ink-faint">FG</th>
          <th class="w-[44px] py-1 pl-1.5 text-right text-[11px] font-normal text-ink-faint">3P</th>
          <th class="w-[36px] py-1 pl-1.5 text-right text-[11px] font-normal text-ink-faint">+/-</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="p in players" :key="p.id" class="border-t-[0.5px] border-hairline">
          <td class="overflow-hidden py-2 text-ellipsis whitespace-nowrap">
            <span class="font-medium text-ink">{{ shortName(p) }}</span>
            <span class="ml-1 text-[11px] text-ink-faint">{{ p.position }}<template v-if="p.jersey_number !== null"> · {{ p.jersey_number }}</template></span>
            <EraBadge
              v-if="activeEra(p.id)"
              class="ml-1.5"
              :name="activeEra(p.id)!.name"
              :rarity="activeEra(p.id)!.rarity"
            />
          </td>
          <td class="py-2 pl-1.5 text-right font-mono text-xs text-ink-dim">{{ p.stats.minutes_played ?? '–' }}</td>
          <td class="py-2 pl-1.5 text-right font-mono text-xs font-medium text-ink">{{ p.stats.points ?? '–' }}</td>
          <td class="py-2 pl-1.5 text-right font-mono text-xs text-ink-dim">{{ p.stats.rebounds ?? '–' }}</td>
          <td class="py-2 pl-1.5 text-right font-mono text-xs text-ink-dim">{{ p.stats.assists ?? '–' }}</td>
          <td class="py-2 pl-1.5 text-right font-mono text-xs text-ink-dim">{{ shots(p.stats.field_goals_made, p.stats.field_goals_attempted) }}</td>
          <td class="py-2 pl-1.5 text-right font-mono text-xs text-ink-dim">{{ shots(p.stats.three_pointers_made, p.stats.three_pointers_attempted) }}</td>
          <td class="py-2 pl-1.5 text-right font-mono text-xs text-ink-dim">{{ plusMinus(p.stats.plus_minus) }}</td>
        </tr>
        <tr v-if="teamStats" class="border-t-[0.5px] border-hairline">
          <td class="py-2 text-[11px] text-ink-faint">Team</td>
          <td class="py-2 pl-1.5 text-right font-mono text-xs text-ink-faint">–</td>
          <td class="py-2 pl-1.5 text-right font-mono text-xs font-medium text-ink">{{ teamStats.points }}</td>
          <td class="py-2 pl-1.5 text-right font-mono text-xs text-ink-dim">{{ teamStats.rebounds }}</td>
          <td class="py-2 pl-1.5 text-right font-mono text-xs text-ink-dim">{{ teamStats.assists }}</td>
          <td class="py-2 pl-1.5 text-right font-mono text-xs text-ink-dim">{{ shots(teamStats.field_goals_made, teamStats.field_goals_attempted) }}</td>
          <td class="py-2 pl-1.5 text-right font-mono text-xs text-ink-dim">{{ shots(teamStats.three_pointers_made, teamStats.three_pointers_attempted) }}</td>
          <td class="py-2 pl-1.5 text-right font-mono text-xs text-ink-dim">–</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
