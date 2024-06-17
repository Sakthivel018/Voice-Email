from OAuth.credential import LANGUAGE
from gtts import gTTS
import os
from playsound import playsound
import speech_recognition as sr

def SpeakText(command, langinp=LANGUAGE):
    if langinp == "": langinp = "en"
    tts = gTTS(text=command, lang=langinp)
    tts.save("~tempfile01.mp3")
    playsound("~tempfile01.mp3")
    print(command)
    os.remove("~tempfile01.mp3")

def speech_to_text():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            print("You said: "+MyText)
            return MyText

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return None

    except sr.UnknownValueError:
        print("unknown error occured")
        return None
