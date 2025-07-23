# your_package/data.py
from pathlib import Path
from yfpy import Data

# Shared Data object
data_dir = Path(__file__).parent.parent / "output"
data = Data(data_dir)

def save_teams(query):
    data.save("my_teams", query.get_user_teams)

def load_teams():
    return data.load("my_teams")
