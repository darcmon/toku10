from fastapi import APIRouter, HTTPException
from typing import List, Optional

from app.schemas import EraDefinition
from app import mock_data

router = APIRouter()

@router.get("/", response_model=List[EraDefinition])
async def list_eras(sport_id: Optional[int] = None):
    """Get the era catalog (names, rarities, trigger thresholds), optionally filtered by sport."""
    return mock_data.get_era_definitions(sport_id)

@router.get("/{era_id}", response_model=EraDefinition)
async def get_era(era_id: int):
    """Get a single era definition"""
    era = mock_data.get_era_definition(era_id)
    if not era:
        raise HTTPException(status_code=404, detail="Era not found")
    return era
