                                               # THIS IS A DESKTOP ASSISSTANT 
                                               # MADE IN PYTHON

import pyttsx3  # pip install pyttsx3 
import speech_recognition as sr  # pip install speechrecognition 
import datetime
import wikipedia   #pip install  wikipedia 
import webbrowser
import os 
import wolframalpha
from time import strftime
engine = pyttsx3.init('sapi5')  
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) 

# function used by jarvis to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# function to wish user on start 
def wishUser():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis How May I Help You")

def takeCommand(): # this  funciton takes input from the user through microphone and returns that as string 

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  
        audio = r.listen(source)

    try: 
        print("Recognizing...")
        query  = r.recognize_google(audio , language='en-in')
        print(f"User said :{query}\n")
         
    except Exception as e:
        print("say that again please...")
        return "None" 
    return query

     

if __name__ == "__main__":
    wishUser()
    
    while True:
        query = takeCommand().lower()
        #logic for executing tasks based on query
        if 'wikipedia' in query :
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)  
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow ' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            webbrowser.open("https://music.youtube.com/watch?v=uhNpl29DGtU&list=RDAMVMuhNpl29DGtU")

        elif 'what is the time' in query:
            Time = datetime.datetime.now(),strftime("%H:%M:%S")
            print(Time)
            speak(f"sir, the time is {Time}")
            
        elif 'open vs code 'in query:
            Path = "C:\\Users\\ayush\\Microsoft VS Code\\Code.exe"
            os.startfile(Path)

        elif 'open chrome' in query:
            tab="C:\\Program Files\\Google\Chrome\\Application\\chrome.exe"
            os.startfile(tab)

        elif 'shutdown my pc'in query:
            speak("shutting the computer")
            os.system("shutdown /s /t 30")

        elif 'jarvis quit' in query:
            speak("Thanks you sir it was nice working with you")
            exit()

        elif 'calculate' in query: 
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)
 
        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)