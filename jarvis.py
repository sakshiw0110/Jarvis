import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') 
print(voices[1].id)

engine.setProperty('voice', voices[0].id)

def speak(audio):
       engine.say(audio)
       engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
              speak("Good morning")
        
    elif hour>=12 and hour<18:
              speak("Good afternoon")

    else:
              speak("Good evening")

    speak("I am jarvis Ma'am. Please tell me how may i help you")
              
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sakshiwaghmare01102001@gmail.com', 'Sakshiw@1')
    server.sendmail('sakshiwaghmare01102001@gmail.com', to, content)
    server.close()

if __name__=="__main__" :
    wishMe()
    # while True:
    if 1:
        query=takeCommand().lower()

    
        if  'wikipedia'  in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open google' in query:
            webbrowser.open("google.com")    
        elif 'open youtube' in query:
              webbrowser.open("youtube.com")
        elif 'play aavesham song' in query:
              webbrowser.open("https://www.youtube.com/watch?v=tOM-nWPcR4U")
        elif 'play music' in query:
            music_dir = 'E:\mummy_mobile\songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to sakshi' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sakshiwaghmare001@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend sakshi bhai. I am not able to send this email")    