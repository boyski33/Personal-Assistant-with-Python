﻿import os, time
import speech_util as speech
import wikipedia
import re

class Wiki:

    def __init__(self):
        self.WIKI_STRING = ""
        self.LENGTH_OF_PLAYBACK = 0
        self.s = speech.SpeechUtil()

    def summary(self, input):
        
        stringToSay = ''

        try:
            stringToSay = wikipedia.summary(input, sentences=1).encode("utf-8")
        except wikipedia.exceptions.DisambiguationError:
            stringToSay = "Be More Specific"
        except wikipedia.exceptions.PageError:
            stringtoSay = "Try Again"

        stringToSay = re.sub(r'(\([^)]*\))', '', stringToSay)
        self.WIKI_STRING = stringToSay

        self.LENGTH_OF_PLAYBACK = self.s.say(stringToSay)
    
    def get_wiki_info(self):
        return self.WIKI_STRING

    def get_length(self):
        return self.LENGTH_OF_PLAYBACK

    def stop(self):
        self.s.stop()
