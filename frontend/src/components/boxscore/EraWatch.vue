<script setup lang="ts">
import { computed, ref } from 'vue'
import type { CurrentEraResponse, EraDefinition } from '../../types/api'
import { api } from '../../lib/api'

const props = defineProps<{
  erasByPlayer: Map<number, CurrentEraResponse>
  eraDefs: Map<number, EraDefinition>
}>()

// Demo identity until auth exists; matches the mock voting user space.
const DEMO_USER_ID = 999

interface WatchItem {
  playerId: number
  playerName: string
  eraId: number
  eraName: string
  rarity: number
  cardTitle: string | null
  submissionId: number | null
  voteCount: number
}

const voteMessage = ref<string | null>(null)
const voteBump = ref(0)

const items = computed<WatchItem[]>(() => {
  const out: WatchItem[] = []
  for (const cur of props.erasByPlayer.values()) {
    if (!cur.active_era) continue
    const def = props.eraDefs.get(cur.active_era.era_id)
    out.push({
      playerId: cur.player_id,
      playerName: cur.player_name,
      eraId: cur.active_era.era_id,
      eraName: cur.active_era.era_name,
      rarity: def?.rarity ?? 1,
      cardTitle: cur.winning_card?.title ?? null,
      submissionId: cur.winning_card?.id ?? null,
      voteCount: (cur.winning_card?.vote_count ?? 0) + (out.length === 0 ? voteBump.value : 0),
    })
  }
  return out.sort((a, b) => b.rarity - a.rarity)
})

const chipStyle = (rarity: number) => {
  if (rarity >= 5) return 'bg-legendary-800 text-legendary-300'
  if (rarity >= 4) return 'bg-epic-900 text-epic-300'
  if (rarity >= 2) return 'bg-rare-900 text-rare-300'
  return 'bg-common-900 text-common-300'
}

const frameStyle = (rarity: number) =>
  rarity >= 5 ? 'border border-legendary-500 bg-legendary-950' : 'border border-arena-700 bg-arena-900'

const gemStyle = (rarity: number) =>
  rarity >= 5
    ? 'border border-legendary-400 bg-legendary-900 text-legendary-300'
    : 'border border-arena-500 bg-arena-900 text-arena-300'

const rarityLabel = (rarity: number) =>
  rarity >= 5 ? 'LGD' : rarity >= 4 ? 'EPC' : rarity >= 2 ? 'RARE' : 'CMN'

async function vote(item: WatchItem) {
  if (item.submissionId === null) return
  try {
    const res = await api.voteOnCard(item.playerId, item.eraId, DEMO_USER_ID, item.submissionId)
    voteMessage.value = res.already_voted
      ? 'Already voted in this era — one vote per era.'
      : 'Vote recorded.'
    if (!res.already_voted) voteBump.value += 1
  } catch {
    voteMessage.value = "Couldn't record the vote. Try again."
  }
}
</script>

<template>
  <div class="px-4 pb-4">
    <div class="rounded-[10px] bg-arena-950 px-5 pt-4 pb-5">
      <div class="mb-3 flex items-baseline justify-between">
        <p class="font-display text-base font-semibold tracking-[0.14em] text-arena-50 uppercase">Era watch</p>
        <span class="text-[11px] text-arena-400">{{ items.length }} active</span>
      </div>

      <div v-if="items.length === 0" class="rounded-[10px] border border-dashed border-arena-600 px-4 py-6 text-center">
        <p class="text-sm text-arena-300">No eras in play for this game yet.</p>
      </div>

      <div v-else class="flex flex-wrap gap-3.5">
        <div
          v-for="(item, idx) in items"
          :key="`${item.playerId}-${item.eraId}`"
          class="flex min-w-[280px] flex-1 items-center gap-3.5 rounded-[10px] p-3.5"
          :class="frameStyle(item.rarity)"
        >
          <div
            class="flex h-[78px] w-[58px] shrink-0 flex-col items-center justify-center rounded-md"
            :class="gemStyle(item.rarity)"
          >
            <span class="font-display text-[15px] font-semibold tracking-[0.14em]">{{ rarityLabel(item.rarity) }}</span>
          </div>
          <div class="min-w-0">
            <span
              class="inline-block rounded-[3px] px-2 py-0.5 text-[10px] font-medium tracking-[0.12em] uppercase"
              :class="chipStyle(item.rarity)"
            >
              {{ item.eraName }}
            </span>
            <p class="mt-1.5 text-sm font-medium text-arena-50">
              {{ item.cardTitle ?? 'No community card yet' }}
            </p>
            <p class="mt-0.5 text-xs text-arena-300">
              {{ item.playerName }}<template v-if="item.cardTitle"> · <span class="font-mono">{{ item.voteCount }}</span> votes</template>
            </p>
            <button
              v-if="idx === 0 && item.submissionId !== null"
              class="mt-2 cursor-pointer rounded border-none bg-gold-400 px-3 py-1 text-[11px] font-medium tracking-wide text-gold-950"
              @click="vote(item)"
            >
              Vote for this card
            </button>
          </div>
        </div>
      </div>

      <p v-if="voteMessage" class="mt-3 text-xs text-arena-300">{{ voteMessage }}</p>
    </div>
  </div>
</template>
