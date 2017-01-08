import os, time
import speech_util as speech
#this is a dummy function

def f(event):

    s = speech.SpeechUtil()
    s.read_the_given_text('This is another text that is being said')
    time.sleep(s.say())
    event.set()