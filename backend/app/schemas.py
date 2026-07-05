# backend/app/schemas.py

from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional

# Sport Schemas
class Sport(BaseModel):
    id: int
    name: str
    code: str

# League Schemas
class League(BaseModel):
    id: int
    sport_id: int
    name: str
    season: str

# Team Schemas
class TeamBase(BaseModel):
    name: str
    abbreviation: Optional[str] = None
    city: Optional[str] = None
    conference: Optional[str] = None
    division: Optional[str] = None

class Team(TeamBase):
    id: int
    league_id: int

# Player Schemas
class PlayerBase(BaseModel):
    first_name: str
    last_name: str
    jersey_number: Optional[int] = None
    position: Optional[str] = None
    height: Optional[int] = Field(default=None, description="Height in cm")
    weight: Optional[int] = Field(default=None, description="Weight in kg")

class Player(PlayerBase):
    id: int
    team_id: Optional[int]

# Game Schemas
class GameBase(BaseModel):
    home_team_id: int
    away_team_id: int
    game_date: datetime
    venue: Optional[str] = None

class Game(GameBase):
    id: int
    league_id: int
    status: str
    home_score: Optional[int] = None
    away_score: Optional[int] = None

# Player Game Stats Schema (Boxscore)
class PlayerGameStatsBase(BaseModel):
    minutes_played: Optional[int] = None
    points: Optional[int] = None
    rebounds: Optional[int] = None
    assists: Optional[int] = None
    steals: Optional[int] = None
    blocks: Optional[int] = None
    turnovers: Optional[int] = None
    fouls: Optional[int] = None
    field_goals_made: Optional[int] = None
    field_goals_attempted: Optional[int] = None
    three_pointers_made: Optional[int] = None
    three_pointers_attempted: Optional[int] = None
    free_throws_made: Optional[int] = None
    free_throws_attempted: Optional[int] = None
    plus_minus: Optional[int] = None
    is_starter: Optional[bool] = False

class PlayerGameStats(PlayerGameStatsBase):
    id: int
    game_id: int
    player_id: int
    team_id: int

# Team Game Stats Schema (team totals for one side of a game)
class TeamGameStatsBase(BaseModel):
    quarter_scores: List[int] = Field(default_factory=list, description="Points per quarter; overtime periods append extra entries")
    points: Optional[int] = None
    rebounds: Optional[int] = None
    assists: Optional[int] = None
    steals: Optional[int] = None
    blocks: Optional[int] = None
    turnovers: Optional[int] = None
    fouls: Optional[int] = None
    field_goals_made: Optional[int] = None
    field_goals_attempted: Optional[int] = None
    three_pointers_made: Optional[int] = None
    three_pointers_attempted: Optional[int] = None
    free_throws_made: Optional[int] = None
    free_throws_attempted: Optional[int] = None

class TeamGameStats(TeamGameStatsBase):
    id: int
    game_id: int
    team_id: int

# Boxscore Response (combines game + stats)
class BoxscorePlayer(Player):
    stats: PlayerGameStats

class BoxscoreResponse(BaseModel):
    game: Game
    home_team: Team
    away_team: Team
    home_team_stats: Optional[TeamGameStats] = None
    away_team_stats: Optional[TeamGameStats] = None
    home_players_stats: List[BoxscorePlayer]
    away_players_stats: List[BoxscorePlayer]

# Era / Card Schemas
class EraDefinition(BaseModel):
    """A catalog entry: an era a player can unlock by crossing a stat threshold."""
    id: int
    sport_id: int
    name: str
    slug: str
    rarity: int
    description: str
    trigger_description: str

class CardSubmission(BaseModel):
    """A community-submitted card image for a (player, era) pairing."""
    id: int
    player_id: int
    era_id: int
    title: Optional[str] = None
    image_url: str
    submitted_by: int
    vote_count: int = 0

class ActiveEra(BaseModel):
    player_id: int
    era_id: int
    era_name: str
    unlocked: bool
    triggered_in_game_id: Optional[int] = None

class CurrentEraResponse(BaseModel):
    player_id: int
    player_name: str
    active_era: Optional[ActiveEra] = None
    winning_card: Optional[CardSubmission] = None
    message: Optional[str] = None

class TriggerResult(BaseModel):
    era_id: int
    era_name: str
    game_id: int
    newly_unlocked: bool

class CheckTriggersResponse(BaseModel):
    player_id: int
    player_name: str
    triggered: List[TriggerResult]

class RoastResponse(BaseModel):
    player_id: int
    player_name: str
    game_id: int
    roast: str

class VoteRequest(BaseModel):
    user_id: int
    submission_id: int

class VoteResponse(BaseModel):
    player_id: int
    era_id: int
    submission_id: int
    user_id: int
    vote_count: int
    already_voted: bool
    message: str
