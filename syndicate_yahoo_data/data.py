def save_teams(query, data):
    data.save("my_teams", query.get_user_teams)