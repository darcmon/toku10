# backend/app/mock_data.py

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

# Mock Team Game Stats (team totals per side; only played games have entries)
MOCK_TEAM_GAME_STATS = [
    {
        "id": 1,
        "game_id": 1,
        "team_id": 1,
        "quarter_scores": [25, 30, 26, 27],
        "points": 108,
        "rebounds": 44,
        "assists": 25,
        "steals": 7,
        "blocks": 5,
        "turnovers": 13,
        "fouls": 18,
        "field_goals_made": 40,
        "field_goals_attempted": 88,
        "three_pointers_made": 12,
        "three_pointers_attempted": 35,
        "free_throws_made": 16,
        "free_throws_attempted": 21
    },
    {
        "id": 2,
        "game_id": 1,
        "team_id": 2,
        "quarter_scores": [29, 27, 31, 28],
        "points": 115,
        "rebounds": 48,
        "assists": 27,
        "steals": 9,
        "blocks": 4,
        "turnovers": 11,
        "fouls": 19,
        "field_goals_made": 42,
        "field_goals_attempted": 90,
        "three_pointers_made": 15,
        "three_pointers_attempted": 38,
        "free_throws_made": 16,
        "free_throws_attempted": 19
    }
]

# === Era system mock data ===================================================

# Catalog of eras, scoped per sport. Each is unlocked when a player's
# single-game stat line crosses the era's threshold (predicates live in
# services/era_engine.py).
ERA_DEFINITIONS = [
    {
        "id": 1,
        "sport_id": 1,
        "name": "MAIN CHARACTER",
        "slug": "main-character",
        "rarity": 5,
        "description": "When the entire game runs through one guy.",
        "trigger_description": "30+ points and 10+ assists in a game",
    },
    {
        "id": 2,
        "sport_id": 1,
        "name": "BUCKET GETTER",
        "slug": "bucket-getter",
        "rarity": 4,
        "description": "Pure scoring takeover.",
        "trigger_description": "40+ points in a game",
    },
    {
        "id": 3,
        "sport_id": 1,
        "name": "DIME LORD",
        "slug": "dime-lord",
        "rarity": 2,
        "description": "Making everyone around them better.",
        "trigger_description": "10+ assists in a game",
    },
    {
        "id": 4,
        "sport_id": 1,
        "name": "GLASS CLEANER",
        "slug": "glass-cleaner",
        "rarity": 3,
        "description": "Owns both backboards.",
        "trigger_description": "15+ rebounds in a game",
    },
    {
        "id": 5,
        "sport_id": 1,
        "name": "TWO-WAY MENACE",
        "slug": "two-way-menace",
        "rarity": 2,
        "description": "Defense travels.",
        "trigger_description": "3+ steals or 3+ blocks in a game",
    },
    {
        "id": 6,
        "sport_id": 1,
        "name": "TRIPLE-DOUBLE",
        "slug": "triple-double",
        "rarity": 5,
        "description": "Double figures, three ways.",
        "trigger_description": "10+ points, 10+ rebounds and 10+ assists in a game",
    },
    {
        "id": 7,
        "sport_id": 1,
        "name": "DOUBLE TROUBLE",
        "slug": "double-trouble",
        "rarity": 1,
        "description": "A tidy double-double.",
        "trigger_description": "10+ in at least two of points, rebounds, assists",
    },
    {
        "id": 8,
        "sport_id": 1,
        "name": "EFFICIENCY GOD",
        "slug": "efficiency-god",
        "rarity": 3,
        "description": "No wasted possessions.",
        "trigger_description": "60%+ field goal shooting on 10+ attempts",
    },
]

# Eras a player has already unlocked. Mutable -- check-triggers appends here.
PLAYER_ERAS = [
    # LeBron earned MAIN CHARACTER earlier in the season...
    {"player_id": 1, "era_id": 1, "triggered_in_game_id": None, "unlocked": True},
    # ...and DIME LORD from game 1 (11 assists).
    {"player_id": 1, "era_id": 3, "triggered_in_game_id": 1, "unlocked": True},
]

# Community-submitted card images for a (player, era). Submission ids are global.
CARD_SUBMISSIONS = [
    {
        "id": 1,
        "player_id": 1,
        "era_id": 1,
        "title": "King's Spotlight",
        "image_url": "https://cards.example.com/lebron/main-character-1.png",
        "submitted_by": 101,
    },
    {
        "id": 2,
        "player_id": 1,
        "era_id": 1,
        "title": "Hollywood Heir",
        "image_url": "https://cards.example.com/lebron/main-character-2.png",
        "submitted_by": 102,
    },
    {
        "id": 3,
        "player_id": 1,
        "era_id": 1,
        "title": "Prime Time",
        "image_url": "https://cards.example.com/lebron/main-character-3.png",
        "submitted_by": 103,
    },
    {
        "id": 4,
        "player_id": 1,
        "era_id": 3,
        "title": "Court Vision",
        "image_url": "https://cards.example.com/lebron/dime-lord-1.png",
        "submitted_by": 104,
    },
]

# Votes cast on submissions. Mutable -- the vote endpoint appends here.
ERA_VOTES = [
    {"user_id": 201, "submission_id": 1},
    {"user_id": 202, "submission_id": 1},
    {"user_id": 203, "submission_id": 2},
]

# Helper functions to query mock data
def get_all_sports() -> List[Dict[str, Any]]:
    return MOCK_SPORTS

def get_sport_by_id(sport_id: int) -> Optional[Dict[str, Any]]:
    return next((sport for sport in MOCK_SPORTS if sport["id"] == sport_id), None)

def get_all_leagues() -> List[Dict[str, Any]]:
    return MOCK_LEAGUES

def get_league_by_id(league_id: int) -> Optional[Dict[str, Any]]:
    return next((league for league in MOCK_LEAGUES if league["id"] == league_id), None)

def get_teams_by_league(league_id: int) -> List[Dict[str, Any]]:
    return [team for team in MOCK_TEAMS if team["league_id"] == league_id]

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

def get_player_all_stats(player_id: int) -> List[Dict[str, Any]]:
    return [stat for stat in MOCK_PLAYER_GAME_STATS if stat["player_id"] == player_id]

def get_team_game_stats(game_id: int) -> List[Dict[str, Any]]:
    return [stat for stat in MOCK_TEAM_GAME_STATS if stat["game_id"] == game_id]

def get_team_stats_for_game(game_id: int, team_id: int) -> Optional[Dict[str, Any]]:
    return next(
        (stat for stat in MOCK_TEAM_GAME_STATS
         if stat["game_id"] == game_id and stat["team_id"] == team_id),
        None
    )

# Era system helpers
def get_era_definitions(sport_id: Optional[int] = None) -> List[Dict[str, Any]]:
    if sport_id is None:
        return ERA_DEFINITIONS
    return [era for era in ERA_DEFINITIONS if era["sport_id"] == sport_id]

def get_era_definition(era_id: int) -> Optional[Dict[str, Any]]:
    return next((era for era in ERA_DEFINITIONS if era["id"] == era_id), None)

def get_player_eras(player_id: int) -> List[Dict[str, Any]]:
    return [pe for pe in PLAYER_ERAS if pe["player_id"] == player_id and pe["unlocked"]]

def has_player_era(player_id: int, era_id: int) -> bool:
    return any(
        pe["player_id"] == player_id and pe["era_id"] == era_id and pe["unlocked"]
        for pe in PLAYER_ERAS
    )

def unlock_player_era(player_id: int, era_id: int, game_id: int) -> bool:
    """Unlock an era for a player. Returns True if it was newly unlocked."""
    if has_player_era(player_id, era_id):
        return False
    PLAYER_ERAS.append(
        {
            "player_id": player_id,
            "era_id": era_id,
            "triggered_in_game_id": game_id,
            "unlocked": True,
        }
    )
    return True

def get_submissions(player_id: int, era_id: int) -> List[Dict[str, Any]]:
    return [
        s for s in CARD_SUBMISSIONS
        if s["player_id"] == player_id and s["era_id"] == era_id
    ]

def get_submission(submission_id: int) -> Optional[Dict[str, Any]]:
    return next((s for s in CARD_SUBMISSIONS if s["id"] == submission_id), None)

def count_votes(submission_id: int) -> int:
    return sum(1 for v in ERA_VOTES if v["submission_id"] == submission_id)

def user_has_voted_in_era(user_id: int, player_id: int, era_id: int) -> bool:
    era_submission_ids = {s["id"] for s in get_submissions(player_id, era_id)}
    return any(
        v["user_id"] == user_id and v["submission_id"] in era_submission_ids
        for v in ERA_VOTES
    )

def add_vote(user_id: int, submission_id: int) -> None:
    ERA_VOTES.append({"user_id": user_id, "submission_id": submission_id})