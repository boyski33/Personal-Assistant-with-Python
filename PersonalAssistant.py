import speech_recognition as sr
import speech_util as speech
import threading
import get_wiki_info
import clock_handler as clock
import weather_handler as weather
from Tkinter import *
import constants

recognizer = sr.Recognizer()
mic = sr.Microphone()
sp = speech.SpeechUtil()

class View:

    def __init__(self, master):
        self.wikiHandler = get_wiki_info.Wiki()
        self.clock = clock.ClockHandler()

        master.geometry("500x200")

        self.frame = Frame(master)
        self.frame.pack()

        self.top_frame = Frame(self.frame)
        self.top_frame.pack(side=TOP)

        self.bottom_frame = Frame(self.frame)
        self.bottom_frame.pack(side = BOTTOM)
        self.status = StringVar()
        self.label = Label(self.top_frame, textvariable=self.status, wraplength=350, justify=LEFT)
        self.label.pack(fill=Y, padx=10, pady=20)

        
        self.btn = Button(self.bottom_frame, text="Listen", command=self.listen_in_background)
        self.btn.pack(side=BOTTOM, pady=20)

    def listen_in_background(self):
        self.btn["state"] = "disabled"
        self.status.set("Listening...")
        self.stopper = recognizer.listen_in_background(mic, self.main, phrase_time_limit=3)

    def listen_for_wiki_query(self):
        self.status.set("Say what you want to search for on Wikipedia: ")
        audio = recognizer.listen(mic, phrase_time_limit=3)
        result = ""
        try:
            result = recognizer.recognize_bing(audio, constants.KEY_BING2)
        except sr.UnknownValueError:
            sp.say("Try again")
        return result
    
    def weather(self):
        w = weather.WeatherHandler()
        length_of_playback = sp.say(w.get_current_weather())
        return length_of_playback


    def wiki(self):
        query = self.listen_for_wiki_query()
        self.status.set("Processing request for: " + query)
        self.wikiHandler.summary(query)
        self.status.set(self.wikiHandler.get_wiki_info())
        return self.wikiHandler.get_length()

    def time(self):
        length_of_playback = sp.say(self.clock.time_now())
        return length_of_playback

    def btn_state_change(self):
         self.btn["state"] = "normal"

    def stop(self):
        self.wikiHandler.stop()
        self.stopper()

    def main(self, recognizer, audio):
        try:
            print "processing request"
            res = recognizer.recognize_bing(audio, key=constants.KEY_BING2, show_all=False)
            res = res.lower()
        
            self.status.set("You said: " + res)

            if res == "wikipedia":
                timeout = self.wiki()
                self.stopper()
                t = threading.Timer(timeout, self.btn_state_change)
                t.start()

            if res == "weather":
                timeout = self.weather()
                self.stopper()
                t = threading.Timer(timeout, self.btn_state_change)
                t.start()


            if res == "time":
                timeout = self.time()
                self.stopper()
                t = threading.Timer(timeout, self.btn_state_change)
                t.start()


            if res == "stop":
                self.stopper()
                print "stopped"

        except LookupError:
            sp.say("Oops! Didn't catch that")

        except sr.UnknownValueError:
            print "Unknown value"

def view():
    root = Tk()
    v = View(root)
    root.mainloop()

if __name__ == "__main__":
    view()