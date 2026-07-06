<script setup lang="ts">
import { computed } from 'vue'
import type { Game, Team } from '../../types/api'

const props = defineProps<{
  game: Game
  homeTeam: Team
  awayTeam: Team
}>()

const homeWon = computed(
  () =>
    props.game.home_score !== null &&
    props.game.away_score !== null &&
    props.game.home_score > props.game.away_score,
)
const awayWon = computed(
  () =>
    props.game.home_score !== null &&
    props.game.away_score !== null &&
    props.game.away_score > props.game.home_score,
)

const dateLabel = computed(() =>
  new Date(props.game.game_date).toLocaleDateString('en-US', { month: 'short', day: 'numeric' }),
)

const statusLabel = computed(() =>
  props.game.status === 'final' ? 'Final' : props.game.status === 'scheduled' ? 'Scheduled' : props.game.status,
)
</script>

<template>
  <div class="flex items-center justify-between px-6 pt-5 pb-4">
    <div class="flex items-center gap-3.5">
      <div
        class="flex h-11 w-11 items-center justify-center rounded-full bg-rare-100 text-[13px] font-medium text-rare-800"
      >
        {{ awayTeam.abbreviation }}
      </div>
      <div>
        <p class="text-[15px] font-medium text-ink">{{ awayTeam.name.split(' ').pop() }}</p>
        <p class="text-xs text-ink-faint">Away<span v-if="awayWon"> · Win</span></p>
      </div>
      <span
        class="ml-2 font-mono text-[34px] font-medium"
        :class="awayWon ? 'text-ink' : 'text-ink-faint'"
      >
        {{ game.away_score ?? '–' }}
      </span>
    </div>

    <div class="text-center">
      <span
        class="inline-block rounded-full border-[0.5px] border-hairline px-2.5 py-0.5 text-[11px] font-medium text-ink-dim"
      >
        {{ statusLabel }}
      </span>
      <p class="mt-1.5 text-xs text-ink-faint">{{ dateLabel }}<span v-if="game.venue"> · {{ game.venue }}</span></p>
    </div>

    <div class="flex items-center gap-3.5">
      <span
        class="mr-2 font-mono text-[34px] font-medium"
        :class="homeWon ? 'text-ink' : 'text-ink-faint'"
      >
        {{ game.home_score ?? '–' }}
      </span>
      <div class="text-right">
        <p class="text-[15px] font-medium text-ink">{{ homeTeam.name.split(' ').pop() }}</p>
        <p class="text-xs text-ink-faint">Home<span v-if="homeWon"> · Win</span></p>
      </div>
      <div
        class="flex h-11 w-11 items-center justify-center rounded-full bg-epic-100 text-[13px] font-medium text-epic-800"
      >
        {{ homeTeam.abbreviation }}
      </div>
    </div>
  </div>
</template>
