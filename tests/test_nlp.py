from src.chatbot import ChatBot

bot = ChatBot("Drax")

#Example tets ssentences to test intent prediction
test_sentences = [
    "Hello there!",
    "hi Drax",
    "goodbye for now",
    "see ya later",
    "how are you doing today?",
    "I'm doing great",
    "Can you help me please?",
    "who made you?",
    "what time is it right now?",
    "tell me a joke",
    "My name is Thor"
]

print("\n NLP Intent Prediction Test:\n")
for text in test_sentences:
    tag = bot.predict_intent(text)
    print(f"Input: {text}  --> Predicted Intent: {tag}")