import asyncio
from bot import logger, CONFIG
from bot.modules.telegram_helper import Bot

BOT_TOKEN = CONFIG["BOT_TOKEN"]
OWNER_ID = CONFIG["OWNER_ID"]
VICTIM_CHAT_ID = CONFIG["VICTIM_CHAT_ID"]

bot = Bot(BOT_TOKEN)

MAIN_MENU_MSG = """
>> tgbot-cli (beta)
====================
1. Send Message
2. print "tgbot-cli"

>> to be continued...

"""

async def main():
    print(MAIN_MENU_MSG)

    while True:
        input_text = input(">> ")

        if input_text == "1":
            message = input("Message: ")
            bot.send_message(OWNER_ID, message)
        elif input_text == "2":
            print("tgbot-cli")


if __name__ == "__main__":
    asyncio.run(main())
