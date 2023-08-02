###########################################
###    USE .ENV FILE OR WRITE URSELF    ###
###########################################

import os
from dotenv import load_dotenv


load_dotenv()

TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_SEND_MESSAGE_WITH_PHOTO_URL = os.getenv('TELEGRAM_SEND_MESSAGE_WITH_PHOTO_URL')
TELEGRAM_SEND_EDITED_MESSAGE = os.getenv('TELEGRAM_SEND_EDITED_MESSAGE')
VK_STANDALONE_APP_TOKEN = os.getenv('VK_STANDALONE_APP_TOKEN')
VK_WALL_GET_URL = os.getenv('VK_WALL_GET_URL')
VK_GROUP_ID = os.getenv('VK_GROUP_ID')
VK_API_VERSION = os.getenv('VK_API_VERSION')