import time
from tools import vk_tools, tg_tools
from tools.sqlite_tools import SqliteTools
import os
from dotenv import load_dotenv
import re

load_dotenv() 

TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
VK_STANDALONE_APP_TOKEN = os.getenv('VK_STANDALONE_APP_TOKEN')
VK_GROUP_ID = os.getenv('VK_GROUP_ID')
VK_API_VERSION = os.getenv('VK_API_VERSION')


def main(vk_parser, tg):
    # tg.send_video()
    while True:
        
        parsed_post = vk_parser.get_last_post()

        parsed_photo = [attachment.photo.sizes[-1].url for attachment in parsed_post.attachments if attachment.photo]
        if not parsed_photo:
            parsed_photo = ["https://sun9-1.userapi.com/impg/uXZRATmrzAcSGgZJtWv21kpGk4Hh-VqNl5Ojrg/cDoJkCzdiZQ.jpg?size=512x512&quality=95&sign=f372f3842854f059316051c07a93a681&type=album"]

        if not SqliteTools.check_exists_post(parsed_post.id):
            re_stirng = (re.findall(r"\[.*?\]", parsed_post.text))
            if re_stirng:
                name = re_stirng[0].split('|')[1][:-1]
                text = name + parsed_post.text[len(re_stirng[0]):]
            else:
                text = parsed_post.text
            message_id = tg.send_message(text=text, photos=parsed_photo)
            SqliteTools.add_post(post_id=parsed_post.id, post_text=text, post_photo=",".join(parsed_photo), telegram_message_id=message_id)
            continue
        
        ### FIX THIS UPDATER ###
        # db_post = SqliteTools.get_post(parsed_post.id)  
        # db_post_photo = db_post.post_photo.split(',')
        # if parsed_post.text != db_post.post_text or parsed_photo != db_post_photo:
        #     tg.update_message(text=parsed_post.text, photos=parsed_photo)
        #     SqliteTools.update_post(post_id=parsed_post.id, text=parsed_post.text, photo=",".join(parsed_photo))

        time.sleep(5)

if __name__ == "__main__":
    vk_parser = vk_tools.VKPostParser(VK_STANDALONE_APP_TOKEN, VK_GROUP_ID, VK_API_VERSION)
    tg = tg_tools.TelegramMessageSenderUpdater(token=TELEGRAM_BOT_TOKEN, chat_id=TELEGRAM_CHAT_ID)
    SqliteTools.check_exists_db()
    main(vk_parser, tg)