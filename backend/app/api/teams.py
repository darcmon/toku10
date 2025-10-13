from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import Team, Player
from app import mock_data

router = APIRouter()

@router.get("/", response_model=List[Team])
async def get_teams():
    """Get all teams"""
    return mock_data.get_all_teams()

@router.get("/{team_id}", response_model=Team)
async def get_team(team_id: int):
    """Get a specific team"""
    team = mock_data.get_team_by_id(team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

@router.get("/{team_id}/players", response_model=List[Player])
async def get_team_roster(team_id: int):
    """Get all players on a team"""
    team = mock_data.get_team_by_id(team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return mock_data.get_players_by_team(team_id)