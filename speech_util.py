import pyglet, os
from gtts import gTTS
import time
import pyttsx

class SpeechUtil(object):

    def __init__(self):
        self.player = pyglet.app
        
    ''' using the Google Text-to-Speech API the string passed_text is processed by the same software 
        used in Google Translate, and is then saved into an mp3 file for later playback. '''
    def read_the_given_text(self, passed_text):
        text = gTTS(text=passed_text, lang='en')
        text.save(os.getcwd() + os.sep + 'text.mp3')

    ''' the text is firstly processed and saved as an mp3 and then played using the pyglet player '''
    def say(self, passed_text):
        self.read_the_given_text(passed_text)
        f = pyglet.media.load(os.getcwd() + os.sep + 'text.mp3', streaming=False)
        f.play()
        return f.duration

    def stop(self):
        self.player.exit()
