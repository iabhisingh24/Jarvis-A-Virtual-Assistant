import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
recognizer = sr.Recognizer()
engine = pyttsx3.init() # to initialize the pyttsx
newsapi = "Your API KEY"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(
        api_key = "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"
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("http://facebook.com")
    elif "open github" in c.lower():
        webbrowser.open("http://github.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("http://linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("http://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("http://instagram.com")
    elif "open chat gpt" in c.lower():
        webbrowser.open("http://chatgpt.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower() :
        r = requests.get(f" https://api.thenewsapi.com/v1/news/top?api_token={newsapi}&locale=us&limit=3")
        if r.status_code == 200:
            headlines_data  = r.json()

            titles = [article['title'] for article in headlines_data['data']]
            speak(titles)    
    else:
        output = aiProcess(c)
        speak(output)
        
if __name__ == "__main__":
    speak("Initializing Jarvis.....")
    speak("Hello Abhinav I am Jarvis ,How Can I help you...")
    while True:
        # Listen for the wake word "Jarvis"...
        # Obtain audio from the microphone.
        r = sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("lisenting....")
                audio = r.listen(source ,timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Yes I'm Listening")
                    
                
                # Listen for command 
                with sr.Microphone() as source:
                    print("Jarvis Active . Listening for the command....")
                    
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    if "tell about me" in command:
                        speak("You are Abhinav. You are currently pursuing BTech in Computer Science, and you are working on Python.")
                    else:
                        speak(f"You said: {command}")
                    

                    processCommand(command)
        except sr.UnknownValueError:
            
            speak("Sorry, I did not catch that.")
        except Exception as e :
            print("Error;{0} ".format(e))
