# 🧾 syndicate_yahoo_data

A Python project that connects to the Yahoo Fantasy Sports API and extracts data such as your fantasy baseball teams and matchups. Data can be saved in JSON format.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/mldrs/fantasy-baseball-stats.git
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows use: .venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

## Setup Environment Variables

To use this script, your own Yahoo Fantasy API is necessary. You can make one here: https://developer.yahoo.com/apps/create/
When you have done this, make a .env file in the root of the directory. Fill in the KEY and SECRET and also fill in your Yahoo League ID. You can find this by clicking on League in the menu of the fantasy app and noting the ID that is displayed at the end of the URL.

```env
YAHOO_CONSUMER_KEY=your_key_here
YAHOO_CONSUMER_SECRET=your_secret_here
LEAGUE_ID=your_league_id_here
```

## Run Scripts

Run the following Python scripts to extract and save data:

### Get my teams

```bash
python scripts/save_teams.py
```

This will save JSON files to the output/ folder.
