import json

SCORE_FILE = "scores.json"

def save_score(user_name, score):
    try:
        with open(SCORE_FILE, "r") as file:
            scores = json.load(file)
    except FileNotFoundError:
        scores = {}

    scores[user_name] = score
    with open(SCORE_FILE, "w") as file:
        json.dump(scores, file)

def get_scores():
    try:
        with open(SCORE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
