import logging

open("chatbot.log", "w").close()

logging.basicConfig(
    filename = "chatbot.log",
    level = logging.INFO,
    format = "%(asctime)s-%(levelname)s-%(message)s"
)

def log_message(user, message):
    logging.info(f"{user}: {message}")