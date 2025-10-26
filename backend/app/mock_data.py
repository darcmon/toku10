# backend/app/mock_data.py

from datetime import datetime
from typing import List, Dict, Any, Optional

# Mock Sports
MOCK_SPORTS = [
    {"id": 1, "name": "Basketball", "code": "NBA"}
]

# Mock Leagues
MOCK_LEAGUES = [
    {"id": 1, "sport_id": 1, "name": "NBA", "season": "2024-25"}
]

# Mock Teams
MOCK_TEAMS = [
    {
        "id": 1,
        "league_id": 1,
        "name": "Los Angeles Lakers",
        "abbreviation": "LAL",
        "city": "Los Angeles",
        "conference": "Western",
        "division": "Pacific"
    },
    {
        "id": 2,
        "league_id": 1,
        "name": "Boston Celtics",
        "abbreviation": "BOS",
        "city": "Boston",
        "conference": "Eastern",
        "division": "Atlantic"
    },
    {
        "id": 3,
        "league_id": 1,
        "name": "Golden State Warriors",
        "abbreviation": "GSW",
        "city": "San Francisco",
        "conference": "Western",
        "division": "Pacific"
    }
]

# Mock Players
MOCK_PLAYERS = [
    {
        "id": 1,
        "team_id": 1,
        "first_name": "LeBron",
        "last_name": "James",
        "jersey_number": 23,
        "position": "SF",
        "height": 206,
        "weight": 113
    },
    {
        "id": 2,
        "team_id": 1,
        "first_name": "Anthony",
        "last_name": "Davis",
        "jersey_number": 3,
        "position": "PF",
        "height": 208,
        "weight": 115
    },
    {
        "id": 3,
        "team_id": 2,
        "first_name": "Jayson",
        "last_name": "Tatum",
        "jersey_number": 0,
        "position": "SF",
        "height": 203,
        "weight": 95
    },
    {
        "id": 4,
        "team_id": 2,
        "first_name": "Jaylen",
        "last_name": "Brown",
        "jersey_number": 7,
        "position": "SG",
        "height": 198,
        "weight": 101
    }
]

# Mock Games
MOCK_GAMES = [
    {
        "id": 1,
        "league_id": 1,
        "home_team_id": 1,
        "away_team_id": 2,
        "game_date": "2024-10-22T19:30:00",
        "status": "final",
        "venue": "Crypto.com Arena",
        "home_score": 108,
        "away_score": 115
    },
    {
        "id": 2,
        "league_id": 1,
        "home_team_id": 3,
        "away_team_id": 1,
        "game_date": "2024-10-25T20:00:00",
        "status": "scheduled",
        "venue": "Chase Center",
        "home_score": None,
        "away_score": None
    }
]

# Mock Player Game Stats (Boxscore data)
MOCK_PLAYER_GAME_STATS = [
    # Game 1 - Lakers vs Celtics
    {
        "id": 1,
        "game_id": 1,
        "player_id": 1,
        "team_id": 1,
        "minutes_played": 38,
        "points": 28,
        "rebounds": 8,
        "assists": 11,
        "steals": 2,
        "blocks": 1,
        "turnovers": 3,
        "fouls": 2,
        "field_goals_made": 10,
        "field_goals_attempted": 20,
        "three_pointers_made": 3,
        "three_pointers_attempted": 8,
        "free_throws_made": 5,
        "free_throws_attempted": 6,
        "plus_minus": -7,
        "is_starter": True
    },
    {
        "id": 2,
        "game_id": 1,
        "player_id": 2,
        "team_id": 1,
        "minutes_played": 35,
        "points": 31,
        "rebounds": 12,
        "assists": 3,
        "steals": 1,
        "blocks": 3,
        "turnovers": 2,
        "fouls": 3,
        "field_goals_made": 12,
        "field_goals_attempted": 22,
        "three_pointers_made": 2,
        "three_pointers_attempted": 5,
        "free_throws_made": 5,
        "free_throws_attempted": 7,
        "plus_minus": -5,
        "is_starter": True
    },
    {
        "id": 3,
        "game_id": 1,
        "player_id": 3,
        "team_id": 2,
        "minutes_played": 40,
        "points": 35,
        "rebounds": 9,
        "assists": 6,
        "steals": 2,
        "blocks": 0,
        "turnovers": 1,
        "fouls": 2,
        "field_goals_made": 13,
        "field_goals_attempted": 24,
        "three_pointers_made": 5,
        "three_pointers_attempted": 11,
        "free_throws_made": 4,
        "free_throws_attempted": 4,
        "plus_minus": 12,
        "is_starter": True
    },
    {
        "id": 4,
        "game_id": 1,
        "player_id": 4,
        "team_id": 2,
        "minutes_played": 37,
        "points": 27,
        "rebounds": 5,
        "assists": 4,
        "steals": 3,
        "blocks": 1,
        "turnovers": 2,
        "fouls": 3,
        "field_goals_made": 10,
        "field_goals_attempted": 18,
        "three_pointers_made": 4,
        "three_pointers_attempted": 9,
        "free_throws_made": 3,
        "free_throws_attempted": 3,
        "plus_minus": 8,
        "is_starter": True
    }
]

# Helper functions to query mock data
def get_all_teams() -> List[Dict[str, Any]]:
    return MOCK_TEAMS

def get_team_by_id(team_id: int) -> Optional[Dict[str, Any]]:
    return next((team for team in MOCK_TEAMS if team["id"] == team_id), None)

def get_players_by_team(team_id: int) -> List[Dict[str, Any]]:
    return [player for player in MOCK_PLAYERS if player["team_id"] == team_id]

def get_player_by_id(player_id: int) -> Optional[Dict[str, Any]]:
    return next((player for player in MOCK_PLAYERS if player["id"] == player_id), None)

def get_all_games() -> List[Dict[str, Any]]:
    return MOCK_GAMES

def get_game_by_id(game_id: int) -> Optional[Dict[str, Any]]:
    return next((game for game in MOCK_GAMES if game["id"] == game_id), None)

def get_game_stats(game_id: int) -> List[Dict[str, Any]]:
    return [stat for stat in MOCK_PLAYER_GAME_STATS if stat["game_id"] == game_id]

def get_player_stats_for_game(game_id: int, player_id: int) -> Optional[Dict[str, Any]]:
    return next(
        (stat for stat in MOCK_PLAYER_GAME_STATS 
         if stat["game_id"] == game_id and stat["player_id"] == player_id),
        None
    )