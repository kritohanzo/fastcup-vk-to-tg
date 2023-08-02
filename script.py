import time
from config import TELEGRAM_CHAT_ID, TELEGRAM_BOT_TOKEN, TELEGRAM_SEND_MESSAGE_WITH_PHOTO_URL, TELEGRAM_SEND_EDITED_MESSAGE, VK_STANDALONE_APP_TOKEN, VK_WALL_GET_URL, VK_GROUP_ID, VK_API_VERSION
from script_tools import VKPostParser, TelegramMessageSenderUpdater
from sqlite_tools import SqliteTools

vk_parser = VKPostParser(VK_STANDALONE_APP_TOKEN, VK_GROUP_ID, VK_API_VERSION)
tg = TelegramMessageSenderUpdater(token=TELEGRAM_BOT_TOKEN, chat_id=TELEGRAM_CHAT_ID)
SqliteTools.check_exists_db()

while True:

    time.sleep(5)

    parsed_post = vk_parser.get_last_post()
    parsed_photo = parsed_post.attachments[0].photo.sizes[-1].url if parsed_post.attachments else 'https://static.vecteezy.com/system/resources/previews/005/337/799/original/icon-image-not-found-free-vector.jpg'

    if not SqliteTools.check_exists_post(parsed_post.id):
        message_id = tg.send_message_with_photo(text=parsed_post.text, photo=parsed_photo)
        SqliteTools.add_post(post_id=parsed_post.id, post_text=parsed_post.text, post_photo=parsed_photo, telegram_message_id=message_id)
        continue
    
    db_post = SqliteTools.get_post(parsed_post.id)  

    if parsed_post.text != db_post.post_text or parsed_photo != db_post.post_photo:
        tg.update_message(message_id=db_post.telegram_message_id, text=parsed_post.text, photo=parsed_photo)
        SqliteTools.update_post(post_id=parsed_post.id, text=parsed_post.text, photo=parsed_photo)
