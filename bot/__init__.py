import os
import json
import logging

with open('log.txt', 'w'):
    pass

#Enable logging
logging.basicConfig(
    filename="log.txt", format="%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(filename)s - %(message)s", level=logging.INFO
)
#set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(filename)s - %(message)s")
console.setFormatter(formatter)
logging.getLogger("").addHandler(console)

logger = logging.getLogger(__name__)

# config
if not os.path.exists("config.json"):
    logger.error("Config file not found.")

    def get_value(prompt):
        value = input(f"{prompt}: ")
        if not value:
            logger.error(f"{prompt} not provided.")
            exit(1)
        return value
    
    bot_token = get_value("BOT Token")
    owner_id = get_value("OwnerID")
    victim_chat_id = get_value("Victim ChatID")

    try:
        tmp_config = {
            "BOT_TOKEN": str(bot_token),
            "OWNER_ID": int(owner_id),
            "VICTIM_CHAT_ID": int(victim_chat_id)
        }
    except TypeError:
        logger.error("You have provided wrong variables.")
        exit(1)
    except Exception as e:
        logger.error(e)
        exit(1)

    with open("config.json", "w") as f:
        json.dump(tmp_config, f, indent=4)

# local storage "config"
CONFIG = {}
with open("config.json", "r") as f:
    CONFIG.update(json.load(f))

logger.info(
"""
𝓐 𝓹𝓻𝓸𝓳𝓮𝓬𝓽 𝓸𝓯

 ▄▄▄▄    ██▓  ██████  ██░ ██  ▄▄▄       ██▓    
▓█████▄ ▓██▒▒██    ▒ ▓██░ ██▒▒████▄    ▓██▒    
▒██▒ ▄██▒██▒░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ▒██░    
▒██░█▀  ░██░  ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ▒██░    
░▓█  ▀█▓░██░▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒░██████▒
░▒▓███▀▒░▓  ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░▓  ░
▒░▒   ░  ▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░░ ░ ▒  ░
 ░    ░  ▒ ░░  ░  ░   ░  ░░ ░  ░   ▒     ░ ░   
 ░       ░        ░   ░  ░  ░      ░  ░    ░  ░
      ░                                        
                            tgbot-cli by bishalqx980
"""
)
