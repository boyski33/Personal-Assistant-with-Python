import speech_recognition as sr
import pprint

KEY = "AIzaSyDhIrlQru9lkHTRgQk4WLBErPptHjfOUDk"
KEY_BING = "e93f74f4ef204c459d79162d9fa3dd76"
KEY_BING2 = "86ab65dede4c41eea14c315ad098ca83"

def callback(recognizer, audio):
    try:
        print "listening"
        res = recognizer.recognize_bing(audio, key = KEY_BING2, show_all=False)
        print "You said: " + res

        if res == "stop":
            print "This will stop the function"
    except LookupError:
        # Fix this to ask the user to repeat the question
        print("Oops! Didn't catch that")
    except sr.UnknownValueError:
        print "Unknown value"
        
recognizer = sr.Recognizer()
recognizer.listen_in_background(sr.Microphone(), callback)

while True:
    pass
