import os
import json
import shutil

# Creating Required Folder/Directories
try:
    for dir_name in ["downloads", "temp", "sys"]:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
        os.makedirs(dir_name, exist_ok=True)
except Exception as e:
    print(e)
    exit(1)

# config
if not os.path.exists("config.json"):
    print("Config file not found.")

    def get_value(prompt):
        value = input(f"{prompt}: ")
        if not value:
            print(f"{prompt} not provided.")
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
        print("You have provided wrong variables.")
        exit(1)
    except Exception as e:
        print(e)
        exit(1)

    with open("config.json", "w") as f:
        json.dump(tmp_config, f, indent=4)

# local storage "config"
CONFIG = {}
with open("config.json", "r") as f:
    CONFIG.update(json.load(f))

print(
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
