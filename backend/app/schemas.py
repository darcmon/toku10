# backend/app/schemas.py

from pydantic import BaseModel
from typing import Optional

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
    height: Optional[int] = None
    weight: Optional[int] = None

class Player(PlayerBase):
    id: int
    team_id: Optional[int]

# Game Schemas
class GameBase(BaseModel):
    home_team_id: int
    away_team_id: int
    game_date: str
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

# Boxscore Response (combines game + stats)
class BoxscorePlayer(Player):
    stats: PlayerGameStats

class BoxscoreResponse(BaseModel):
    game: Game
    home_team: Team
    away_team: Team
    home_players_stats: list[BoxscorePlayer]
    away_players_stats: list[BoxscorePlayer]