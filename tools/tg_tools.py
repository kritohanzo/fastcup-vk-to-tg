import telebot


class TelegramMessageSenderUpdater:

    def __init__(self, token, chat_id):
        self.session = telebot.TeleBot(token=token)
        self.chat_id = chat_id

    def send_message(self, text, photos):
        if len(photos) > 1:
            response = self.session.send_media_group(chat_id=self.chat_id, media=[telebot.types.InputMediaPhoto(media=photo) for photo in photos])
            self.session.edit_message_caption(caption=text, chat_id=self.chat_id, message_id=response[0].message_id)
            return response[0].message_id
        else:
            response = self.session.send_photo(chat_id=self.chat_id, photo=photos[0], caption=text)
            return response.message_id

    # def send_video(self):
    #     self.session.send_media_group(chat_id=self.chat_id, media=[telebot.types.InputMediaVideo(media="https://vk.com/video-197998355_456240582")])
    
    ### FIX THIS ###
    # def update_message(self, text, photos=None):
    #     if len(self.last_response) > 1:
    #         for message in self.last_response:  
    #             self.session.edit_message_media(chat_id=self.chat_id, message_id=message.message_id, media=telebot.types.InputMediaPhoto(media=photos[0]))
    #         self.session.edit_message_caption(chat_id=self.chat_id, message_id=self.last_response[0].message_id, caption=text)