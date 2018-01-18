import requests


def get_team_map():
    mods = requests.get(
        "https://api.utopian.io/api/moderators").json()["results"]
    return {m["account"]: m.get("referrer", m["account"]) for m in mods}
