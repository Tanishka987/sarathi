import pyttsx3
import speech_recognition
from subprocess import call

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

rate = engine.setProperty("rate",170)

def autonomous():
    call(['python','autonomous/1.py'])

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source,0,4)
    try:
        print("Understanding..")
        query = r.recognize_google(audio, language="en-IN")
        print(f"You Said:{query}\n")
    except Exception as e:
        print("Say that again")
        return ""
    return query

if __name__ == "__main__":
    speak('Welcome to Autonomous Wheelchair')
    speak('This chair is equipped with numerous features')

    query = takeCommand().lower()

    if 'navigate' in query:
        autonomous()
    elif "hello chair" in query:
        speak("Sarthik mae aapka swagat hai")
        from GreetMe import greetMe
        greetMe()
    
        while True:
            query = takeCommand().lower()
            if "go to sleep" in query :
                speak("Ok sir! You can call me anytime")
                break
            elif "hello" in query:
                speak("Hello sir, how are you?")
            elif "i am fine" in query:
                speak("that's great sir")
            elif "how are you" in query:
                speak("Perfect, sir")
            elif "thank you" in query:
                speak("you are welcome, sir")
            elif "navigate" in query:
                autonomous()
                break
            elif "google" in query:
                from SearchNow import searchGoogle
    
                searchGoogle(query)
            elif "youtube" in query:
                from SearchNow import searchYoutube
    
                searchYoutube(query)
            elif "wikipedia" in query:
                from SearchNow import searchWikipedia
    
                searchWikipedia(query)
        

