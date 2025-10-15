import json
import re
import os
from datetime import datetime

class ChatBot:
    def __init__(self, name="PyBot", intents_file="data/intents.json"):
        self.name = name
        self.intents = self.load_intents()

    def load_intents(self):
        intents_path = os.path.join(os.path.dirname(__file__), "..", "data", "intents.json")
        try:
            with open(intents_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print("json file not found.")
            return {}

    def get_response(self, user_input):
        for pattern, response in self.intents.items():
            if re.search(pattern, user_input, re.IGNORECASE):
                response = response.replace("{time}", datetime.now().strftime("%H:%M:%S"))
                response = response.replace("{date}", datetime.now().strftime("%Y-%m-%d"))
                response = response.replace("{name}", self.name)
                return response
            
        return "I'm not sure how to respond to that."

if __name__ == "__main__":
    bot = ChatBot("Drax")
    print("Drax: Hello! Type exit to quit")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Drax out.")
            break
        print(f"Drax: {bot.get_response(user_input)}\n")