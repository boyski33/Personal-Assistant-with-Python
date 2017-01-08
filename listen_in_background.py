import speech_recognition as sr
import multiprocessing, os

def listen(recognizer, source, callback, event, running=True):
    assert isinstance(source, sr.AudioSource), "Source must be an audio source"

    with source as s:
        while running:
            try:
                audio = recognizer.listen(s, phrase_time_limit=3)       
            except WaitTimeoutError: # listening timed out, just try again
                pass
            else:
                event.wait()
                callback(recognizer, audio)