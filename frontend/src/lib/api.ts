import type {
  BoxscoreResponse,
  CurrentEraResponse,
  EraDefinition,
  VoteResponse,
} from '../types/api'

const BASE = import.meta.env.VITE_API_BASE ?? '/api/v1'

async function get<T>(path: string): Promise<T> {
  const res = await fetch(`${BASE}${path}`)
  if (!res.ok) throw new Error(`GET ${path} failed: ${res.status}`)
  return res.json()
}

async function post<T>(path: string, body?: unknown): Promise<T> {
  const res = await fetch(`${BASE}${path}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: body === undefined ? undefined : JSON.stringify(body),
  })
  if (!res.ok) throw new Error(`POST ${path} failed: ${res.status}`)
  return res.json()
}

export const api = {
  getBoxscore: (gameId: number) => get<BoxscoreResponse>(`/games/${gameId}/boxscore`),
  getEras: () => get<EraDefinition[]>('/eras/'),
  getPlayerCurrentEra: (playerId: number) =>
    get<CurrentEraResponse>(`/players/${playerId}/current`),
  voteOnCard: (playerId: number, eraId: number, userId: number, submissionId: number) =>
    post<VoteResponse>(`/players/${playerId}/era/${eraId}/vote`, {
      user_id: userId,
      submission_id: submissionId,
    }),
}
