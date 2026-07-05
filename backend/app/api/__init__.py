from fastapi import APIRouter
from .sports import router as sports_router
from .leagues import router as leagues_router
from .teams import router as teams_router
from .games import router as games_router
from .players import router as players_router
from .eras import router as eras_router

router = APIRouter()

router.include_router(sports_router, prefix="/sports", tags=["sports"])
router.include_router(leagues_router, prefix="/leagues", tags=["leagues"])
router.include_router(teams_router, prefix="/teams", tags=["teams"])
router.include_router(games_router, prefix="/games", tags=["games"])
router.include_router(players_router, prefix="/players", tags=["players"])
router.include_router(eras_router, prefix="/eras", tags=["eras"])