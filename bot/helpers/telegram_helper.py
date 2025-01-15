import time
import requests

def send_req(bot_token, method, data=dict, files=None):
    starting_time = time.time()
    print("Execution started...")
    API_URL = f"https://api.telegram.org/bot{bot_token}"
    try:
        r = requests.get(f"{API_URL}/{method}", data, files=files) 
        if r.status_code != 200:
            print(r.content)
        end_time = time.time()
        print(f"Execution time: {(end_time - starting_time):.2f}s")
        return r
    except Exception as e:
        print(e)

class Bot:
    def __init__(self, bot_token):
        self.bot_token = bot_token


    def send_message(self, chat_id, text):
        data = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "HTML"
        }

        r = send_req(self.bot_token, "sendMessage", data)
        return r.content
    

    def send_audio(self, chat_id, audio_path, title, caption=None):
        data = {
            "chat_id": chat_id,
            "title": title
        }

        if caption:
            data.update({"caption": caption})

        with open(audio_path, "rb") as f:
            audio = {"audio": f.read()}

        r = send_req(self.bot_token, "sendAudio", data, audio)
        return r.content
