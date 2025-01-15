import os
import shutil
from bot import CONFIG
from bot.helpers.telegram_helper import Bot
from bot.helpers.data.data import MESSAGES
from bot.modules.gtts import tts
from bot.modules.ytdlp import youtube_download

BOT_TOKEN = CONFIG["BOT_TOKEN"]
OWNER_ID = CONFIG["OWNER_ID"]
VICTIM_CHAT_ID = CONFIG["VICTIM_CHAT_ID"]

bot = Bot(BOT_TOKEN)

# main func
def main():
    print(MESSAGES.MAIN_MENU_MESSAGE)

    while True:
        input_text = input(">> ")

        if input_text == "0":
            print(MESSAGES.MAIN_MENU_MESSAGE)
        
        elif input_text == "1":
            message = input("Message: ")
            bot.send_message(VICTIM_CHAT_ID, message)
            print("Execution done!")
        
        elif input_text == "2":
            text = input("Text to convert: ")
            accent = input("Voice accent (default 'en'): ") or "en"
            tts(text, accent)
            print("Execution done!")
        
        elif input_text == "3":
            url = input("YouTube URL: ")
            if url:
                tg_upload = input("Upload to telegram? (y/n): ")
                tg_upload = True if tg_upload == "y" else False
                response = youtube_download(url, tg_upload)
                
                if tg_upload:
                    bot.send_audio(VICTIM_CHAT_ID, response["file_path"], response["file_name"], response["file_name"])

                print("Execution done!")
            else:
                print("No url was given!")
        
        elif input_text == "clear":
            try:
                for dir_name in ["downloads", "temp", "sys"]:
                    if os.path.exists(dir_name):
                        shutil.rmtree(dir_name)
                    os.makedirs(dir_name, exist_ok=True)
                print("Execution done!")
            except Exception as e:
                print(e)
                exit(1)

        elif input_text == "q":
            break
        
        else:
            print("Wrong input!")


if __name__ == "__main__":
    main()
