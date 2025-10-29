from src.chatbot import ChatBot
import time, sys

def type_effect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def run_chat():
    bot = ChatBot("Drax")
    print("Drax: Hello! Type exit to quit \n")

    if bot.user_name:
        print(f"Drax: Welcome back, {bot.user_name}!\n")

    while True:
        user_input = input("You: ").strip()
        if(user_input.lower() == "exit"):
            type_effect("Drax out.")
            break
        response = bot.get_response(user_input)
        print("Drax: ", end="")
        type_effect(response)
        print()