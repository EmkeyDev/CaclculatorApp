import json
import os

HISTORY_FILE = "history.json"

class HistoryManager:
    def __init__(self):
        self.history = self.load()

    def load(self):
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, "r") as f:
                return json.load(f)
        return []

    def save(self):
        with open(HISTORY_FILE, "w") as f:
            json.dump(self.history, f)

    def add(self, expression, result):
        record = f"{expression} = {result}"
        self.history.append(record)
        self.save()
        return record

    def delete(self, index):
        if 0 <= index < len(self.history):
            self.history.pop(index)
            self.save()

    def clear(self):
        self.history = []
        self.save()

    def get_all(self):
        return self.history
