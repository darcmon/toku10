# backend/app/services/era_engine.py
#
# Era engine: evaluates stat-threshold triggers, tallies community votes on
# card-image submissions, and generates game roasts.
#
# Written for Python 3.9 -- no PEP 604 (X | None) unions; uses typing.Optional.

from typing import List, Dict, Any, Optional

from app import mock_data


# --- Small stat accessors (treat missing/None as 0) -------------------------
def _pts(s: Dict[str, Any]) -> int:
    return s.get("points") or 0


def _reb(s: Dict[str, Any]) -> int:
    return s.get("rebounds") or 0


def _ast(s: Dict[str, Any]) -> int:
    return s.get("assists") or 0


def _stl(s: Dict[str, Any]) -> int:
    return s.get("steals") or 0


def _blk(s: Dict[str, Any]) -> int:
    return s.get("blocks") or 0


def _double_count(s: Dict[str, Any]) -> int:
    """How many of points/rebounds/assists are in double figures."""
    return sum(1 for v in (_pts(s), _reb(s), _ast(s)) if v >= 10)


def _fg_pct(s: Dict[str, Any]) -> float:
    fga = s.get("field_goals_attempted") or 0
    if fga == 0:
        return 0.0
    return (s.get("field_goals_made") or 0) / fga


# --- Trigger predicates -----------------------------------------------------
# Each takes a single-game stat line and returns True if it unlocks the era.
# Keyed by era id (see mock_data.ERA_DEFINITIONS for the matching metadata).
# Predicates are basketball-specific; when other sports are added, key this
# per sport alongside the sport-scoped era catalog.
TRIGGER_PREDICATES = {
    1: lambda s: _pts(s) >= 30 and _ast(s) >= 10,                        # MAIN CHARACTER
    2: lambda s: _pts(s) >= 40,                                          # BUCKET GETTER
    3: lambda s: _ast(s) >= 10,                                          # DIME LORD
    4: lambda s: _reb(s) >= 15,                                          # GLASS CLEANER
    5: lambda s: _stl(s) >= 3 or _blk(s) >= 3,                           # TWO-WAY MENACE
    6: lambda s: _pts(s) >= 10 and _reb(s) >= 10 and _ast(s) >= 10,      # TRIPLE-DOUBLE
    7: lambda s: _double_count(s) >= 2,                                  # DOUBLE TROUBLE
    8: lambda s: _fg_pct(s) >= 0.60 and (s.get("field_goals_attempted") or 0) >= 10,  # EFFICIENCY GOD
}


def get_era_definition(era_id: int) -> Optional[Dict[str, Any]]:
    return mock_data.get_era_definition(era_id)


def evaluate_game(stats: Dict[str, Any]) -> List[int]:
    """Return the era ids unlocked by a single game stat line."""
    return [era_id for era_id, predicate in TRIGGER_PREDICATES.items() if predicate(stats)]


def check_triggers(player_id: int) -> List[Dict[str, Any]]:
    """Evaluate all of a player's games and unlock any newly-triggered eras.

    Returns one result per (game, era) hit, marking whether it was newly unlocked.
    """
    results: List[Dict[str, Any]] = []
    for stats in mock_data.get_player_all_stats(player_id):
        for era_id in evaluate_game(stats):
            era = get_era_definition(era_id)
            newly_unlocked = mock_data.unlock_player_era(
                player_id, era_id, stats["game_id"]
            )
            results.append(
                {
                    "era_id": era_id,
                    "era_name": era["name"] if era else "UNKNOWN",
                    "game_id": stats["game_id"],
                    "newly_unlocked": newly_unlocked,
                }
            )
    return results


def get_winning_card(player_id: int, era_id: int) -> Optional[Dict[str, Any]]:
    """The top-voted card submission for a (player, era), or None."""
    submissions = mock_data.get_submissions(player_id, era_id)
    if not submissions:
        return None
    enriched = [
        {**s, "vote_count": mock_data.count_votes(s["id"])} for s in submissions
    ]
    return max(enriched, key=lambda s: s["vote_count"])


def get_current_era(player_id: int) -> Optional[Dict[str, Any]]:
    """The player's currently-active era (rarest unlocked) plus its winning card."""
    eras = mock_data.get_player_eras(player_id)
    if not eras:
        return None

    def _rarity(player_era: Dict[str, Any]) -> int:
        definition = get_era_definition(player_era["era_id"])
        return definition["rarity"] if definition else 0

    active = max(eras, key=lambda pe: (_rarity(pe), pe["era_id"]))
    era_def = get_era_definition(active["era_id"])
    winning_card = get_winning_card(player_id, active["era_id"])
    return {"player_era": active, "era_def": era_def, "winning_card": winning_card}


def record_vote(
    player_id: int, era_id: int, user_id: int, submission_id: int
) -> Dict[str, Any]:
    """Record a vote for a submission. One vote per user per (player, era).

    Returns a result dict; on validation failure it contains an "error" key.
    """
    submission = mock_data.get_submission(submission_id)
    if (
        not submission
        or submission["player_id"] != player_id
        or submission["era_id"] != era_id
    ):
        return {"error": "Submission not found for this player and era"}

    already_voted = mock_data.user_has_voted_in_era(user_id, player_id, era_id)
    if not already_voted:
        mock_data.add_vote(user_id, submission_id)
        message = "Vote recorded."
    else:
        message = "You have already voted in this era; only one vote per era is allowed."

    return {
        "player_id": player_id,
        "era_id": era_id,
        "submission_id": submission_id,
        "user_id": user_id,
        "vote_count": mock_data.count_votes(submission_id),
        "already_voted": already_voted,
        "message": message,
    }


# --- Roast generation -------------------------------------------------------
def _player_game_result(player: Dict[str, Any], game: Dict[str, Any]) -> Optional[str]:
    """'win' / 'loss' / None for the player's team in this game."""
    team_id = player.get("team_id")
    home_score = game.get("home_score")
    away_score = game.get("away_score")
    if home_score is None or away_score is None:
        return None
    if team_id == game.get("home_team_id"):
        return "win" if home_score > away_score else "loss"
    if team_id == game.get("away_team_id"):
        return "win" if away_score > home_score else "loss"
    return None


def generate_roast(
    player: Dict[str, Any], stats: Dict[str, Any], game: Dict[str, Any]
) -> str:
    """Build a playful roast from a player's stat line in a given game."""
    pts, reb, ast = _pts(stats), _reb(stats), _ast(stats)
    turnovers = stats.get("turnovers") or 0
    fouls = stats.get("fouls") or 0
    plus_minus = stats.get("plus_minus")
    fga = stats.get("field_goals_attempted") or 0
    fgm = stats.get("field_goals_made") or 0
    minutes = stats.get("minutes_played") or 0
    pct = _fg_pct(stats)

    lines: List[str] = []

    if fga >= 10 and pct < 0.40:
        lines.append(
            f"{fgm}-of-{fga} from the field ({round(pct * 100)}%) -- the rim filed a restraining order."
        )
    if turnovers >= 4:
        lines.append(
            f"{turnovers} turnovers; the ball spent more time with the other team than your own."
        )
    if plus_minus is not None and plus_minus < 0:
        lines.append(
            f"A {plus_minus} plus/minus -- the scoreboard actively got worse every time you checked in."
        )
    if fouls >= 5:
        lines.append(f"{fouls} fouls -- 'defense' apparently means grabbing.")
    if minutes >= 20 and pts < 10:
        lines.append(
            f"{pts} points in {minutes} minutes. The box score nearly forgot you suited up."
        )

    if _player_game_result(player, game) == "loss":
        lines.append(
            f"And the team still lost -- a {pts}/{reb}/{ast} line looks great until you check the W/L column."
        )

    if not lines:
        name = f"{player['first_name']} {player['last_name']}"
        suffix = " in a win" if _player_game_result(player, game) == "win" else ""
        return (
            f"Tried to roast {name} and came up empty: {pts} pts, {reb} reb, {ast} ast"
            f"{suffix}. Clean line, no notes -- the kitchen's closed."
        )

    return " ".join(lines)
