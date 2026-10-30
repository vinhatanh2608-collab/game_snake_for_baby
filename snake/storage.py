import json
import os

FILENAME = "high_score.json"


class StorageManager:
    def __init__(self, filename=FILENAME):
        self.filename = filename

    def load_high_score(self):
        if not os.path.exists(self.filename):
            return 0
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("high_score", 0)
        except (json.JSONDecodeError, IOError):
            return 0

    def save_high_score(self, score):
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump({"high_score": score}, f, indent=4)
        except IOError:
            pass