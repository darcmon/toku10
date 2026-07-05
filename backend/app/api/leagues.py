from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import League, Team
from app import mock_data

router = APIRouter()

@router.get("/", response_model=List[League])
async def get_leagues():
    """Get all leagues"""
    return mock_data.get_all_leagues()

@router.get("/{league_id}", response_model=League)
async def get_league(league_id: int):
    """Get a specific league"""
    league = mock_data.get_league_by_id(league_id)
    if not league:
        raise HTTPException(status_code=404, detail="League not found")
    return league

@router.get("/{league_id}/teams", response_model=List[Team])
async def get_league_teams(league_id: int):
    """Get all teams in a league"""
    league = mock_data.get_league_by_id(league_id)
    if not league:
        raise HTTPException(status_code=404, detail="League not found")
    return mock_data.get_teams_by_league(league_id)
