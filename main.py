import pyttsx3
import speech_recognition as sr
from emotions import wishMe, initiate, sad, happy, mood
from features import wiki, playonyt, whois, time, easter01, location, temperature, write, read, news, highlights, weather, calculator, breaker, newsSound, coinSound, flip
from mapmaker import myMap

# ---------- Engine Creation --------------
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 145)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# ---------- Input Command -----------------
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        #query = "hey what's up"
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        speak("i didn't get that sir...")
        return "none"

    return query


def taskExecution():
    #initiate()
    #wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()
        query = query.replace("none", "")

        if "wiki" in query:
            wiki(query)

        if "who is" in query:
            whois(query)

        if "play" in query:
            playonyt(query)

        if "time" in query:
            time()

        if "who are you" in query:
            easter01()

        if "location" in query:
            location()

        if "temperature" in query:
            temperature(query)

        if "remember that" in query:
            write(query)

        if "what do you remember" in query:
            read()

        if "news" in query:
            newsSound()
            news()

        if "highlights" in query:
            newsSound()
            highlights()

        if "weather" in query:
            weather(query)

        if "calculate" in query:
            calculator(query)

        if "thanks" in query:
            breaker()

        if "sad" in query:
            sad()

        if "how are you" in query:
            mood()

        if "flip a coin" in query:
            coinSound()
            flip()

        if "map" in query:
            myMap()

        else:
            #speak("i am not sure about that..")
            print("Error: A34")


print("system initiating....")
wishMe()
while True:
    query = takeCommand().lower()
    query = query.replace("none", "")
    if "friday" in query:
        taskExecution()
