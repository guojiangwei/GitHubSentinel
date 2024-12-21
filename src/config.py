import json

class Config:
    @staticmethod
    def load():
        with open("config.json", "r") as file:
            return json.load(file)
