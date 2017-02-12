import pyglet, os
from gtts import gTTS
import time
import pyttsx

class SpeechUtil(object):

    def __init__(self):
        self.player = pyglet.app

    def read_the_given_text(self, passed_text):
        text = gTTS(text=passed_text, lang='en')
        text.save(os.getcwd() + os.sep + 'text.mp3')

# Plays the audio
    def say(self, passed_text):
        self.read_the_given_text(passed_text)
        f = pyglet.media.load(os.getcwd() + os.sep + 'text.mp3', streaming=False)
        f.play()
        return f.duration

    def stop(self):
        self.player.exit()