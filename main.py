import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary
import requests
from openai import OpenAI


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "<Your Key Here>"  #Use your own api key OR ELSE U can test out other features

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):

    client = OpenAI(
        api_key="<Your Key Here>"  # Replace with your actual API key
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or gpt-3.5-turbo, gpt-4-turbo depending on your plan
        messages=[
            {"role": "system", "content": "You are a virtual assistant named JARVIS skilled in general tasks like Alexa and Google Cloud. Give short responses"},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
    )

    print(completion.choices[0].message.content)


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open amazon" in c.lower():
        webbrowser.open("https://www.amazon.in")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.ger(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            #parse the JSON response
            data = r.json()

            #Extract the articles in the list
            articles = data.get('articles',[])

            #Speak the headlines in News
            for article in articles:
                speak(article["title"])

    else:
        #Let openAI do the work
        output = aiProcess(c)
        speak(output)


if __name__  == "__main__": 
    speak("Initializing Jarvis")
    while True:
    # Listen for the wake word Jarvis
        r = sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout = 2, phrase_time_limit = 1)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("yeah")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))
