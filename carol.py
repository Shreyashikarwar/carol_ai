import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)

engine.setProperty('voice', voices[1].id)


# sperak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# if __name__ == "__main__":
#     speak("Hello Shreyash Boss. How may I help you?")

# wish function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<16:
        speak("Good Afternoon!")
    elif hour>=16 and hour<22:
        speak("Good Evening!")
    else:
        speak("Good Night")
    speak("I am Carol. Tell me how may i help you.")

# if __name__ == "__main__":
#     wishMe()

def takecommand():
    """it take microphone input from user and return sting output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 #seconds of non speaking time between reply from carol
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("email@gmail.com", "email@123")
    server.sendmail("email@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()

    #logic for executing 
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results =  wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stactoverflow.com')
        elif 'play video' in query:
            video_dir = 'D:\\Video songs'
            video = os.listdir(video_dir)
            os.startfile(os.path.join(video_dir,video[0]))
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" Shreyash the time is {strtime}")
        elif 'open code' in query:
            codepath = "C:\\Users\\shrey\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'open pycharm' in query:
            pycharmpath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.2\\bin\\pycharm64.exe"
            os.startfile(pycharmpath)
        elif 'open photos' in query:
            photos_dir = "D:\\Camera"
            pic = os.listdir(photos_dir)
            os.startfile(os.path.join(photos_dir,pic[0]))
        elif 'email to harry' in query:
            try:
                speak('What should I say?')
                content = takecommand()
                to = "shreyashsikarwar2020@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry boss I am not able to send the email!")
        elif 'exit' in query:
            exit