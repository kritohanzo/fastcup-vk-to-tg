from .pydantic_models import Items
import vk_api


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