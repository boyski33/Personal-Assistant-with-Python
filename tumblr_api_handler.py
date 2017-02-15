import pytumblr
from tumblr_keys import *
from constants import SINGLE_LOCAL_PHOTO, MULTIPLE_LOCAL_PHOTOS, \
    SINGLE_URL_SOURCE_PHOTO, EMBEDDED_VIDEO, LOCAL_VIDEO

''' Post different types of Tumblr posts '''
class TumblrAPIHandler(object):
    def __init__(self):
        #create a client using the given keys from the tumblr API
        self.client = pytumblr.TumblrRestClient(
            consumer_key, consumer_secret,
            token_key, token_secret)
        self.blogname = 'nbupythonproject.tumblr.com'

    def make_a_text_post(self, message_body, list_of_tags, title,
                         state='published'):
        self.client.create_text(self.blogname, body=message_body, title=title,
                                state=state, tags=list_of_tags)

    def make_a_photo_post(self, type_of_photo_post, list_of_tags,
                          state='published', url_photo=None, local_photo=None):
        if type_of_photo_post == SINGLE_LOCAL_PHOTO or \
                        type_of_photo_post == MULTIPLE_LOCAL_PHOTOS:
            self.client.create_photo(self.blogname, state=state,
                                     tags=list_of_tags, data=local_photo)
        elif type_of_photo_post == SINGLE_URL_SOURCE_PHOTO:
            self.client.create_photo(self.blogname,  state=state,
                                    tags=list_of_tags, source=url_photo)

    def make_a_quote_post(self, list_of_tags, quote,
                          source, state='published'):
        self.client.create_quote(self.blogname, state=state, tags=list_of_tags,
                                 quote=quote, source=source)

    def make_a_chat_post(self, chat, list_of_tags, title, state='published'):
        self.client.create_chat(self.blogname, conversation=chat,
                                tags=list_of_tags, title=title, state=state)

    def make_a_link_post(self, list_of_tags, title, description, url,
                         state='published'):
        self.client.create_link(self.blogname, description=description,
                                tags=list_of_tags, title=title, url=url,
                                state=state)

    def make_an_audio_post(self, caption, list_of_tags, source,
                           state='published'):
        self.client.create_audio(self.blogname, caption=caption,
                                 tags=list_of_tags, state=state,
                                 external_url=source)

    def make_a_video_post(self, caption, list_of_tags, source,
                          type_of_video, state='published'):
        if type_of_video == EMBEDDED_VIDEO:
            self.client.create_video(self.blogname, caption=caption,
                                     tags=list_of_tags, embed=source,
                                     state=state)
        elif type_of_video == LOCAL_VIDEO:
            self.client.create_video(self.blogname, caption=caption,
                                     tags=list_of_tags, embed=source,
                                     state=state)

    def get_dashboard_info(self):
        return self.client.dashboard()

