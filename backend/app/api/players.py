from fastapi import APIRouter, HTTPException
from typing import List

from app.schemas import (
    Player,
    CurrentEraResponse,
    RoastResponse,
    CheckTriggersResponse,
    VoteRequest,
    VoteResponse,
)
from app import mock_data
from app.services import era_engine

router = APIRouter()


def _player_name(player: dict) -> str:
    return f"{player['first_name']} {player['last_name']}"


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


@router.get("/{player_id}/current", response_model=CurrentEraResponse)
async def get_current_era(player_id: int):
    """Get the player's currently-active era and its community-winning card."""
    player = mock_data.get_player_by_id(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    name = _player_name(player)
    current = era_engine.get_current_era(player_id)
    if not current:
        return CurrentEraResponse(
            player_id=player_id,
            player_name=name,
            active_era=None,
            winning_card=None,
            message="No eras unlocked yet. Ball out to earn one.",
        )

    era_def = current["era_def"]
    active_era = {
        "player_id": player_id,
        "era_id": era_def["id"],
        "era_name": era_def["name"],
        "unlocked": True,
        "triggered_in_game_id": current["player_era"].get("triggered_in_game_id"),
    }
    return CurrentEraResponse(
        player_id=player_id,
        player_name=name,
        active_era=active_era,
        winning_card=current["winning_card"],
        message=f"Current era: {era_def['name']}",
    )


@router.get("/{player_id}/roast", response_model=RoastResponse)
async def roast_player(player_id: int, game_id: int):
    """Roast a player based on their stat line in a given game."""
    player = mock_data.get_player_by_id(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    game = mock_data.get_game_by_id(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")

    stats = mock_data.get_player_stats_for_game(game_id, player_id)
    if not stats:
        raise HTTPException(
            status_code=404, detail="No stats for this player in this game"
        )

    roast = era_engine.generate_roast(player, stats, game)
    return RoastResponse(
        player_id=player_id,
        player_name=_player_name(player),
        game_id=game_id,
        roast=roast,
    )


@router.post("/{player_id}/check-triggers", response_model=CheckTriggersResponse)
async def check_triggers(player_id: int):
    """Evaluate the player's games and unlock any newly-triggered eras."""
    player = mock_data.get_player_by_id(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    triggered = era_engine.check_triggers(player_id)
    return CheckTriggersResponse(
        player_id=player_id,
        player_name=_player_name(player),
        triggered=triggered,
    )


@router.post("/{player_id}/era/{era_id}/vote", response_model=VoteResponse)
async def vote_on_card(player_id: int, era_id: int, vote: VoteRequest):
    """Cast a vote for a card submission in a player's era."""
    player = mock_data.get_player_by_id(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    era = mock_data.get_era_definition(era_id)
    if not era:
        raise HTTPException(status_code=404, detail="Era not found")

    result = era_engine.record_vote(player_id, era_id, vote.user_id, vote.submission_id)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result
