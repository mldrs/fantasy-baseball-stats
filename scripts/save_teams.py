from syndicate_yahoo_data.query import get_query
from syndicate_yahoo_data.data import save_teams

query = get_query()
save_teams(query)
print("Teams saved.")