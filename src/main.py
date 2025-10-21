from src.chatbot import ChatBot

def run_chat():
    bot = ChatBot("Drax")
    print("Drax: Hello! Type exit to quit \n")

    if bot.user_name:
        print(f"Drax: Welcome back, {bot.user_name}!\n")

    while True:
        user_input = input("You: ").strip()
        if(user_input.lower() == "exit"):
            print("Drax out.")
            break
        print(f"Drax: {bot.get_response(user_input)}\n")