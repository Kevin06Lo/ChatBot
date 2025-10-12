import json
from utils import log_message

class ChatBot:
    def __init__(self, name="PyBot", intents_path="data/intents.json"):
        self.name = name
        with open(intents_path, "r") as f:
            self.intents = json.load(f)

    def get_response(self, user_input):
        text = user_input.lower()
        if any(word in text for word in self.intents["greetings"]):
            return "Hello! How can I help you?"
        elif any(word in text for word in self.intents["farewells"]):
            return "Goodbye!! Have a great day!"
        elif any(word in text for word in self.intents["thanks"]):
            return "You are welcome!"
        else:
            return "I'm not sure how to respond yet"

if __name__ == "__main__":
    bot = ChatBot()
    while True:
        user_input = input("You: ")
        log_message("user", user_input)
        if user_input.lower() == "exit":
            break
        response = bot.get_response(user_input)
        print(f"Bot: {response}")
        log_message("bot", response)