import pyglet
from gtts import gTTS

class SpeechUtil(object):

    def __init__(self):
        self.player = pyglet.media

    def read_the_given_text(self, passed_text):
        text = gTTS(text=passed_text, lang='en')
        text.save('text.mp3')

    def say(self):
        f = self.player.load('text.mp3', streaming=False)
        f.play()