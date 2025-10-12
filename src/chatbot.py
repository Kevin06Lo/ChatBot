class ChatBot:
    def __init__(self, name="PyBot"):
        self.name = name

    def get_response(self, user_input):
        user_input = user_input.lower()
        if "hello" in user_input:
            return "Hi there! How can I help you today?"
        elif "bye" in user_input:
            return "Goodbye! Have a great day!"
        else:
            return "I'm not sure how to respond yet."

if __name__ == "__main__":
    bot = ChatBot()
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Bye!")
            break
        print(f"Bot: {bot.get_response(user_input)}")    