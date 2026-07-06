// Mirrors backend/app/schemas.py

export interface Team {
  id: number
  league_id: number
  name: string
  abbreviation: string | null
  city: string | null
  conference: string | null
  division: string | null
}

export interface Player {
  id: number
  team_id: number | null
  first_name: string
  last_name: string
  jersey_number: number | null
  position: string | null
  height: number | null // cm
  weight: number | null // kg
}

export interface Game {
  id: number
  league_id: number
  home_team_id: number
  away_team_id: number
  game_date: string
  venue: string | null
  status: string
  home_score: number | null
  away_score: number | null
}

export interface PlayerGameStats {
  id: number
  game_id: number
  player_id: number
  team_id: number
  minutes_played: number | null
  points: number | null
  rebounds: number | null
  assists: number | null
  steals: number | null
  blocks: number | null
  turnovers: number | null
  fouls: number | null
  field_goals_made: number | null
  field_goals_attempted: number | null
  three_pointers_made: number | null
  three_pointers_attempted: number | null
  free_throws_made: number | null
  free_throws_attempted: number | null
  plus_minus: number | null
  is_starter: boolean | null
}

export interface TeamGameStats {
  id: number
  game_id: number
  team_id: number
  quarter_scores: number[]
  points: number | null
  rebounds: number | null
  assists: number | null
  steals: number | null
  blocks: number | null
  turnovers: number | null
  fouls: number | null
  field_goals_made: number | null
  field_goals_attempted: number | null
  three_pointers_made: number | null
  three_pointers_attempted: number | null
  free_throws_made: number | null
  free_throws_attempted: number | null
}

export interface BoxscorePlayer extends Player {
  stats: PlayerGameStats
}

export interface BoxscoreResponse {
  game: Game
  home_team: Team
  away_team: Team
  home_team_stats: TeamGameStats | null
  away_team_stats: TeamGameStats | null
  home_players_stats: BoxscorePlayer[]
  away_players_stats: BoxscorePlayer[]
}

export interface EraDefinition {
  id: number
  sport_id: number
  name: string
  slug: string
  rarity: number
  description: string
  trigger_description: string
}

export interface CardSubmission {
  id: number
  player_id: number
  era_id: number
  title: string | null
  image_url: string
  submitted_by: number
  vote_count: number
}

export interface ActiveEra {
  player_id: number
  era_id: number
  era_name: string
  unlocked: boolean
  triggered_in_game_id: number | null
}

export interface CurrentEraResponse {
  player_id: number
  player_name: string
  active_era: ActiveEra | null
  winning_card: CardSubmission | null
  message: string | null
}

export interface VoteResponse {
  player_id: number
  era_id: number
  submission_id: number
  user_id: number
  vote_count: number
  already_voted: boolean
  message: string
}
