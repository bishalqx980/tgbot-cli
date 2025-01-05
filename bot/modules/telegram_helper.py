import time
import requests
from bot import logger

def send_req(bot_token, method, data=dict):
    starting_time = time.time()
    logger.info("Execution started...")
    API_URL = f"https://api.telegram.org/bot{bot_token}"
    try:
        r = requests.get(f"{API_URL}/{method}", data)
        end_time = time.time()
        logger.info(f"Execution time: {(end_time - starting_time):.2f}s")
        return r
    except Exception as e:
        logger.error(e)

class Bot:
    def __init__(self, bot_token):
        self.bot_token = bot_token


    def send_message(self, chat_id, text):
        data = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "MARKDOWN"
        }

        r = send_req(self.bot_token, "sendMessage", data)
        return r.content
