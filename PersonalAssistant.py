import speech_recognition as sr
import multiprocessing, os
from get_wiki_data import *
import speech_util as s

KEY = "AIzaSyDhIrlQru9lkHTRgQk4WLBErPptHjfOUDk"
KEY_BING = "e93f74f4ef204c459d79162d9fa3dd76"
KEY_BING2 = "86ab65dede4c41eea14c315ad098ca83"

recognizer = sr.Recognizer()
speech = s.SpeechUtil()

def main(recognizer, audio):
    try:
        print "processing request"
        res = recognizer.recognize_bing(audio, key = KEY_BING2, show_all=False)
        res = res.lower()
        
        print "You said: " + res

        if res[0:2] == "ok":
            speech.read_the_given_text('initialized')
            speech.say()
            
        if res == "stop":
            print "stop"

    except LookupError:
        # Fix this to ask the user to repeat the question
        print("Oops! Didn't catch that")
        speech.read_the_given_text("Oops! Didn't catch that")
        speech.say()
    except sr.UnknownValueError:
        print "Unknown value"

     
recognizer = sr.Recognizer()
recognizer.listen_in_background(sr.Microphone(), main)

while True:
    pass
    