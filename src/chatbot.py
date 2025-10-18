import json
import re
import os
import random
from datetime import datetime

class ChatBot:
    def __init__(self, name="PyBot"):
        self.name = name
        self.intents = self.load_intents()

    def load_intents(self):
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        intents_path = os.path.join(base_dir, "data", "intents.json")
        try:
            with open(intents_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data.get("intents", [])
        except FileNotFoundError:
            print("json file not found.")
            return []

    def get_response(self, user_input):
        for intent in self.intents:
            for pattern in intent["patterns"]:
                if re.search(pattern, user_input, re.IGNORECASE):
                    response = random.choice(intent["responses"])
                    response = response.replace("{time}", datetime.now().strftime("%H:%M"))
                    response = response.replace("{date}", datetime.now().strftime("%Y-%m-%d"))
                    response = response.replace("{name}", self.name)
                    return response
            
        return "I'm not sure how to respond to that."

if __name__ == "__main__":
    bot = ChatBot("Drax")
    print("Drax: Hello! Type exit to quit. \n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Drax out.")
            break
        print(f"Drax: {bot.get_response(user_input)}\n")