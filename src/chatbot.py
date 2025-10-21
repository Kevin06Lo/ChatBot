import json
import re
import os
import random
from datetime import datetime

class ChatBot:
    def __init__(self, name="PyBot"):
        self.name = name
        self.user_name = self.load_memory().get("user_name", None)
        self.intents = self.load_intents()
        self.memory = []

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
    
    def load_memory(self):
        memory_path = os.path.join(os.path.dirname(__file__), "..", "data", "memory.json")
        if os.path.exists(memory_path):
            with open(memory_path, "r", encoding="utf-8") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return {}
        return {}
    
    def save_memory(self):
        memory_path = os.path.join(os.path.dirname(__file__), "..", "data", "memory.json")
        with open(memory_path, "w", encoding="utf-8") as file:
            json.dump({"user_name": self.user_name}, file)


    def remember(self, role, message):
        self.memory.append({"role": role, "message": message})
        if len(self.memory) > 10:
            self.memory.pop(0)
    
    def get_last_user_message(self, skip_current=False):
        user_messages = [m["message"] for m in self.memory if m["role"] == "user"]
        if not user_messages:
            return None
        return user_messages[-2] if skip_current and len(user_messages) > 1 else user_messages[-1]

    def get_response(self, user_input):
        self.remember("user", user_input)
        last_user_msg = self.get_last_user_message(skip_current=True) or ""
        name_match = re.search(r"my name is (.*)", user_input, re.IGNORECASE)

        if name_match:
            user_name = name_match.group(1).strip().capitalize()
            self.user_name = user_name
            self.save_memory()
            self.remember("user_name", self.user_name)
            response = random.choice([
                f"Nice to meet you, {user_name}!", 
                f"Hello, {user_name}",
                f"Happy to have you here {user_name}!"
                ])
            self.remember("bot", response)
            return response    

        if "who created you" in (last_user_msg or "").lower() and "what language" in user_input.lower():
            response = "Python of course!"
            self.remember("bot", response)
            return response

        for intent in self.intents:
            for pattern in intent["patterns"]:
                if re.search(pattern, user_input, re.IGNORECASE):
                    response = random.choice(intent["responses"])
                    response = response.replace("{time}", datetime.now().strftime("%H:%M"))
                    response = response.replace("{date}", datetime.now().strftime("%Y-%m-%d"))
                    response = response.replace("{name}", self.name)

                    if self.user_name:
                        response = response.replace("{user_name}", self.user_name)

                    self.remember("bot", response)
                    return response
            
        reponse = "I'm not sure how to respond to that."
        self.remember("bot", response)
        return reponse