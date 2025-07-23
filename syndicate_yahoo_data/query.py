from pathlib import Path
from yfpy.query import YahooFantasySportsQuery
from syndicate_yahoo_data.auth import get_league_id

def get_query() -> YahooFantasySportsQuery:
    return YahooFantasySportsQuery(
        league_id=get_league_id(),
        game_code="mlb",
        save_token_data_to_env_file=True,
        env_file_location=Path(__file__).parent.parent
    )
