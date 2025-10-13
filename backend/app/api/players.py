from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import Player
from app import mock_data

router = APIRouter()

@router.get("/", response_model=List[Player])
async def get_players():
    """Get all players"""
    return mock_data.MOCK_PLAYERS

@router.get("/{player_id}", response_model=Player)
async def get_player(player_id: int):
    """Get a specific player"""
    player = mock_data.get_player_by_id(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player