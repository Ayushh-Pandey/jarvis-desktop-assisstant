import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from time import strftime
# import pyaudio
engine = pyttsx3.init('sapi5') # used for using voices
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis How May I Help You")
def takeCommand(): # it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 #agr bolte mey gap aaye 1 sec ka toh complete na krde phase
        #enegy threshold bdha skte h taki extra voice jarvis na sune
        #control click on pausetheshold to open class
        audio = r.listen(source)

    try: 
        print("Recognizing...")
        query  = r.recognize_google(audio , language='en-in')
        print(f"User said :{query}\n")
        # we are recognizing command as given
    
    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None" #simple string not python wala none
    return query

    #funtion audio le ra h microphone aur usse string mey return kr ra h agr na sune ton none return kr ra h
# def sendEmail(to,content):
#     server=smtp.SMTP('')
if __name__ == "__main__":
    wishMe()
    
    while True:
        query = takeCommand().lower()
        #logic for executing tasks based on query
        if 'wikipedia' in query :
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)#sentences jitne equal rhegi utna bolega wiki krke
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

        elif 'the time' in query:
            strTime = datetime.datetime.now(),strftime("%H:%M:%S")
            print(strTime)
            speak(f"sir, the time is {strTime}")
            
        elif 'open vs code 'in query:
            codePath = "C:\\Users\\ayush\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open chrome' in query:
            tab="C:\\Program Files\\Google\Chrome\\Application\\chrome.exe"
            os.startfile(tab)
        
        elif 'jarvis quit' in query:
            break