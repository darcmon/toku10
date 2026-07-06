<script setup lang="ts">
import { onMounted, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import type { BoxscoreResponse, CurrentEraResponse, EraDefinition } from '../types/api'
import { api } from '../lib/api'
import GameHeader from '../components/boxscore/GameHeader.vue'
import LineScore from '../components/boxscore/LineScore.vue'
import TeamComparison from '../components/boxscore/TeamComparison.vue'
import PlayerStatTable from '../components/boxscore/PlayerStatTable.vue'
import EraWatch from '../components/boxscore/EraWatch.vue'

const route = useRoute()

const boxscore = ref<BoxscoreResponse | null>(null)
const erasByPlayer = ref<Map<number, CurrentEraResponse>>(new Map())
const eraDefs = ref<Map<number, EraDefinition>>(new Map())
const loading = ref(true)
const error = ref<string | null>(null)

async function load() {
  loading.value = true
  error.value = null
  try {
    const gameId = Number(route.params.gameId)
    const [box, defs] = await Promise.all([api.getBoxscore(gameId), api.getEras()])
    boxscore.value = box
    eraDefs.value = new Map(defs.map((d) => [d.id, d]))

    const players = [...box.away_players_stats, ...box.home_players_stats]
    const currents = await Promise.all(players.map((p) => api.getPlayerCurrentEra(p.id)))
    erasByPlayer.value = new Map(currents.map((c) => [c.player_id, c]))
  } catch (e) {
    error.value = e instanceof Error ? e.message : 'Failed to load boxscore'
  } finally {
    loading.value = false
  }
}

onMounted(load)
watch(() => route.params.gameId, load)
</script>

<template>
  <div class="mx-auto max-w-3xl px-4 py-6">
    <div v-if="loading" class="py-16 text-center text-sm text-ink-faint">Loading boxscore…</div>

    <div v-else-if="error" class="py-16 text-center">
      <p class="text-sm text-ink-dim">Couldn't load this game.</p>
      <p class="mt-1 font-mono text-xs text-ink-faint">{{ error }}</p>
      <button
        class="mt-4 cursor-pointer rounded border-[0.5px] border-hairline bg-paper px-3 py-1.5 text-xs text-ink-dim"
        @click="load"
      >
        Retry
      </button>
    </div>

    <div
      v-else-if="boxscore"
      class="overflow-hidden rounded-xl border-[0.5px] border-hairline bg-paper"
    >
      <GameHeader
        :game="boxscore.game"
        :home-team="boxscore.home_team"
        :away-team="boxscore.away_team"
      />

      <LineScore
        v-if="boxscore.away_team_stats && boxscore.home_team_stats"
        :away-abbr="boxscore.away_team.abbreviation ?? 'AWY'"
        :home-abbr="boxscore.home_team.abbreviation ?? 'HOM'"
        :away-stats="boxscore.away_team_stats"
        :home-stats="boxscore.home_team_stats"
      />

      <TeamComparison
        v-if="boxscore.away_team_stats && boxscore.home_team_stats"
        :away-stats="boxscore.away_team_stats"
        :home-stats="boxscore.home_team_stats"
      />

      <div class="space-y-4 border-t-[0.5px] border-hairline px-6 py-4">
        <PlayerStatTable
          :team-name="boxscore.away_team.name"
          :players="boxscore.away_players_stats"
          :team-stats="boxscore.away_team_stats"
          :eras-by-player="erasByPlayer"
          :era-defs="eraDefs"
        />
        <PlayerStatTable
          :team-name="boxscore.home_team.name"
          :players="boxscore.home_players_stats"
          :team-stats="boxscore.home_team_stats"
          :eras-by-player="erasByPlayer"
          :era-defs="eraDefs"
        />
        <p class="text-[11px] text-ink-faint">
          Badges show each player's rarest unlocked era · legendary tier gets the dark treatment
        </p>
      </div>

      <EraWatch :eras-by-player="erasByPlayer" :era-defs="eraDefs" />
    </div>
  </div>
</template>
