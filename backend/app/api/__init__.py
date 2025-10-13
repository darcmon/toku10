from fastapi import APIRouter
from .teams import router as teams_router
from .games import router as games_router
from .players import router as players_router

router = APIRouter()

router.include_router(teams_router, prefix="/teams", tags=["teams"])
router.include_router(games_router, prefix="/games", tags=["games"])
router.include_router(players_router, prefix="/players", tags=["players"])

# Import and include route modules here
# from .users import router as users_router
# router.include_router(users_router, prefix="/users", tags=["users"])