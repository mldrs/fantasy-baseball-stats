from pathlib import Path
from dotenv import load_dotenv
from yfpy import Data

from syndicate_yahoo_data.query import get_query
from syndicate_yahoo_data.data import save_teams

load_dotenv()

query = get_query()
output_dir = Path(__file__).resolve().parent.parent / "output"
data = Data(output_dir)

save_teams(query, data)
#save_matchups(query)
print("✅ Data updated.")
