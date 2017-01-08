import speech_recognition as sr
import multiprocessing, os
import listen_in_background as lb
import debug

# CONSTANTS
KEY_GOOGLE = "AIzaSyDhIrlQru9lkHTRgQk4WLBErPptHjfOUDk"
KEY_BING = "e93f74f4ef204c459d79162d9fa3dd76"
KEY_BING2 = "86ab65dede4c41eea14c315ad098ca83"


recognizer = sr.Recognizer()
mic = sr.Microphone()
event = multiprocessing.Event()

# This function needs to be defined as the multiprocessing module
# needs every called function to be pickable
# read this: https://goo.gl/yZSS3w
def listen(event):
    lb.listen(recognizer, mic, main, event)

def main(recognizer, audio):

    try:
        print "processing request"
        res = recognizer.recognize_bing(audio, key=KEY_BING2, show_all=False)
        res = res.lower()
        
        print "You said: " + res

        if res[0:2] == "ok":
            debug.f(event)

        if res == "stop":
            print "stop"

    except LookupError:
        print("Oops! Didn't catch that")

    except sr.UnknownValueError:
        print "Unknown value"

if __name__ == '__main__':

    p = multiprocessing.Process(target=listen, args=(event,))
    p.start()
    event.set()
    while True:
        pass
    p.join()