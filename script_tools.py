from pydantic_models import Items
import vk_api
import telebot

class VKPostParser:
    last_post_id = None

    def __init__(self, token, group_id, api_version):
        self.session = vk_api.VkApi(token=token, api_version=api_version)
        self.api = self.session.get_api()
        self.group_id = group_id
    
    def get_last_post(self):
        posts = Items(**self.api.wall.get(owner_id=self.group_id, count=2))
        if not posts.items[0].is_pinned:
            return posts.items[0]
        return posts.items[1]

class TelegramMessageSenderUpdater:

    def __init__(self, token, chat_id):
        self.session = telebot.TeleBot(token=token)
        self.chat_id = chat_id

    def send_message_with_photo(self, text, photo):
        response = self.session.send_photo(chat_id=self.chat_id, caption=text, photo=photo)
        return response.message_id

    def update_message(self, message_id, text, photo=None):
        self.session.edit_message_media(chat_id=self.chat_id, message_id=message_id, media=telebot.types.InputMediaPhoto(photo))
        self.session.edit_message_caption(chat_id=self.chat_id, message_id=message_id, caption=text)