import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent.parent / ".env")

def get_league_id():
    return os.getenv("LEAGUE_ID")
