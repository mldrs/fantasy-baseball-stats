from pathlib import Path
from yfpy import Data
from yfpy.logger import get_logger
from yfpy.query import YahooFantasySportsQuery
#from yfpy.models import OAuth2Yahoo

# Load environment
import os
from dotenv import load_dotenv

load_dotenv()

league_id = os.getenv("LEAGUE_ID")
print(league_id)

query = YahooFantasySportsQuery(
    league_id=league_id,
    game_code="mlb",
    save_token_data_to_env_file=True,
    env_file_location=Path(".")
)

games = query.get_user_games()

for game in games:
    print(game)