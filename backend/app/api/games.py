from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import Game, PlayerGameStats, BoxscoreResponse, BoxscorePlayer
from app import mock_data

router = APIRouter()

@router.get("/", response_model=List[Game])
async def get_games():
    """Get all games"""
    return mock_data.get_all_games()

@router.get("/{game_id}", response_model=Game)
async def get_game(game_id: int):
    """Get a specific game"""
    game = mock_data.get_game_by_id(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game

@router.get("/{game_id}/stats", response_model=List[PlayerGameStats])
async def get_game_stats(game_id: int):
    """Get all player stats for a game"""
    game = mock_data.get_game_by_id(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return mock_data.get_game_stats(game_id)

@router.get("/{game_id}/boxscore", response_model=BoxscoreResponse)
async def get_boxscore(game_id: int):
    """Get complete boxscore for a game"""
    game = mock_data.get_game_by_id(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    
    home_team = mock_data.get_team_by_id(game["home_team_id"])
    away_team = mock_data.get_team_by_id(game["away_team_id"])
    all_stats = mock_data.get_game_stats(game_id)
    
    # Separate home and away player stats
    home_stats = [s for s in all_stats if s["team_id"] == game["home_team_id"]]
    away_stats = [s for s in all_stats if s["team_id"] == game["away_team_id"]]
    
    # Combine player info with stats
    home_players_stats = []
    for stat in home_stats:
        player = mock_data.get_player_by_id(stat["player_id"])
        home_players_stats.append({**player, "stats": stat})
    
    away_players_stats = []
    for stat in away_stats:
        player = mock_data.get_player_by_id(stat["player_id"])
        away_players_stats.append({**player, "stats": stat})
    
    return {
        "game": game,
        "home_team": home_team,
        "away_team": away_team,
        "home_players_stats": home_players_stats,
        "away_players_stats": away_players_stats
    }