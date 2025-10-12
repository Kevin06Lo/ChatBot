from src.chatbot import ChatBot

def test_greeting():
    bot = ChatBot()
    response = bot.get_response("hello")
    assert "hi" in response.lower()