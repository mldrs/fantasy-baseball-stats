from flask import Blueprint, render_template, jsonify
import json
from pathlib import Path

main = Blueprint("main", __name__)

@main.route("/")
def show_json():
    json_path = Path(__file__).parent.parent.parent / "output" / "my_teams.json"
    with open(json_path, "r") as f:
        json_data = json.load(f)
    return render_template("json_viewer.html", data=json_data)

@main.route("/json")
def serve_json():
    json_path = Path(__file__).parent.parent.parent / "output" / "my_teams.json"
    with open(json_path, "r") as f:
        json_data = json.load(f)
    return jsonify(json_data)

@main.route("/teams")
def show_teams_table():
    json_path = Path(__file__).parent.parent.parent / "output" / "my_teams.json"
    with open(json_path, "r") as f:
        raw_data = json.load(f)
    
    teams = []
    for team in raw_data:
        teams.append({
            "league": team["game"]["code"],
            "season": team["game"]["season"],
            "teamname": team["game"]["teams"]["team"]["name"],
            "manager": team["game"]["teams"]["team"]["managers"]["manager"]["nickname"]
        })

    return render_template("teams_table.html", teams=teams)