import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

from HealthyProgrammer import programmer

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)

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
        speak("Good Evening!")  

    speak("Hii, I am Vignesh. Please tell me how may I help you")    

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
   

if __name__=="__main__":
    wishMe()
    query = takeCommand().lower()
    if 'healthy day' in query:
            print("\n***** Start day with healthy mode, have a greate day *****\n")
            speak("Start day with healthy mode, have a greate day")
            init_water =programmer.time()
            init_eyes = programmer.time()
            init_exercise = programmer.time()
            watersecs = 40*60
            exsecs = 50*60
            eyessecs = 30*60

            while True:
                query = takeCommand().lower()
                if programmer.time() - init_water > watersecs:
                    print("Water Drinking time. (Enter 'd' to stop the alarm & 'x' to exit.)")
                    programmer.musiconloop('./HealthyProgrammer/water.mp3')
                    init_water = programmer.time()
                    programmer.log_now("water","Drank Water at")

                if programmer.time() - init_eyes >eyessecs:
                    print("Eye exercise time. (Enter 'd' to stop the alarm & 'x' to exit.)")
                    programmer.musiconloop('./HealthyProgrammer/eyes.mp3')
                    init_eyes = programmer.time()
                    programmer.log_now("eyes","Eyes Relaxed at")

                if programmer.time() - init_exercise > exsecs:
                    print("Physical Activity Time. (Enter 'd' to stop the alarm & 'x' to exit.) ")
                    programmer.musiconloop('./HealthyProgrammer/physical.mp3')
                    init_exercise = programmer.time()
                    programmer.log_now("physical","Physical Activity done at")

    # while True:
    # # if 1:
    #     query = takeCommand().lower()

        # Logic for executing tasks based on query
                if 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                
                elif 'go to youtube' in query:
                    webbrowser.open("youtube.com")

                elif 'open google' in query:
                    webbrowser.open("google.com")

                elif 'open stackoverflow' in query:
                    webbrowser.open("stackoverflow.com")   

                elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"Sir, the time is {strTime}")

                elif 'open my code' in query:
                    codePath = "C:\\Users\\vsasp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)

                elif 'what is your name' in query:
                    speak('my name is vighnesh')

                elif 'who are you' in query:
                    speak('I am Vignesh\'s assistant. He coded me')

                elif 'exit' in query:
                    speak('good Bye')
                    quit()
                
                    
                elif 'shutdown' in query:
                    speak('are you sure, do you want to shutdown computer')
                    query = takeCommand().lower()
                    if 's' in query:
                        os.system("shutdown /s /t 1")
                    

                elif 'restart' in query:
                    speak('are you sure, do you want to restart computer')
                    query = takeCommand().lower()
                    if 'yes' in query:
                        os.system("shutdown /r /t 1")
                
           






        