from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import Sport, League
from app import mock_data

router = APIRouter()

@router.get("/", response_model=List[Sport])
async def get_sports():
    """Get all sports"""
    return mock_data.get_all_sports()

@router.get("/{sport_id}", response_model=Sport)
async def get_sport(sport_id: int):
    """Get a specific sport"""
    sport = mock_data.get_sport_by_id(sport_id)
    if not sport:
        raise HTTPException(status_code=404, detail="Sport not found")
    return sport

@router.get("/{sport_id}/leagues", response_model=List[League])
async def get_sport_leagues(sport_id: int):
    """Get all leagues for a sport"""
    sport = mock_data.get_sport_by_id(sport_id)
    if not sport:
        raise HTTPException(status_code=404, detail="Sport not found")
    return [l for l in mock_data.get_all_leagues() if l["sport_id"] == sport_id]
