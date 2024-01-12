import pyttsx3  
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os 
import smtplib
import time
# from playsound import playsound
import openai
import pyjokes
import requests
from bs4 import BeautifulSoup



engine = pyttsx3.init('sapi5')  #sapi5
voices = engine.getProperty('voices')
# print(voices)
# print(voices[0].id)  1,0
engine.setProperty('voices',voices[0].id)


# speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#wish function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Jarvis. Please tell me how may I help you")

# take command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1   # for experiment
        audio = r.listen(source)
# exception
    try:
        print("Recognize.....")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please....")
        return "None"
    return query

# for email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gamil.com',587)
    server.ehlo()
    server.starttls()
    server.login('singhnaru68@gmail.com','password')
    server.sendmail('singhnaru68@gmail.com',to,content)
    server.close()

# personal details
def personaldetails():
    print("\n*********** Enter Your details ***************")
    name = input("Full name:")
    mobile = input("Mobile Number:")
    email = input("Your Mail:")
    address = input("Enter your address:")
    city = input("City:")  # Use '=' instead of ':'
    state = input("State:")  # Use '=' instead of ':'
    country = input("Country:")  # Use '=' instead of ':'
    pincode = input("Pincode:")
    print("\n************ Your details ***************")
    print("Username - " + name)
    print("Mobile - " + mobile)
    print("Email - " + email)
    print("Address - " + address)
    print("City - " + city)
    print("State - " + state)
    print("Country - " + country)
    print("Pincode - " + pincode)
    print("\n*****************************************")
# message
if __name__ == "__main__":
    # name = input("Enter you name:")
    # speak("Hello"+name)
    personaldetails()
    wishMe()
    while True:
        query = takeCommand().lower()
        # logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        # daily things
        elif 'google' in query:
            speak('Searching google...')
            query = query.replace("google","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to google")
            print(results)
            speak(results)
            webbrowser.open("google.com")
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open whatsapp' in query:
            webbrowser.open("whatsappweb.com")
        
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open w3school' in query:
            webbrowser.open("w3schools.com")
        
        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open chat gpt' in query:
            webbrowser.open("chat.openai.com")    
      

        # normal talking
        elif 'who are you' in query:
            speak("hey i am small jarvis program")

        elif 'what are you doing' in query:
            speak("i am helping human")
        
        elif 'i need you' in query:
            speak("yes,i am always with you")

        elif 'i love you' in query:
            speak("i love you to")
        
        elif 'i hate you' in query:
            speak("but I love you")
        
        elif 'i kill you' in query:
            speak("why not..! try it")
        
        elif 'i want hug you' in query:
            speak("why not..")
        
        elif 'can i hug you' in query:
            speak("why not...")
        
        elif 'i want kiss you' in query:
            speak("sure")
        
        elif 'can i kiss you' in query:
            speak("sure")
        
        elif 'i am suffering from fever' in query:
            speak("o no")
            speak("please take food")
            speak("than after take medicine")
            speak("and take rest")
            speak("take care")
            speak("can i call doc or mom")

        elif 'what do you want' in query:
            speak("i want do your wishes")
                
        elif 'who i am ' in query:
            speak("you are a human")
        
        elif 'where are you from' in query:
            speak("i am currently live in a laptop")

        elif 'thank you jarvis' in query:
            speak("you welcome")
        
        elif 'thank you' in query:
            speak("you welcome")

        elif 'okay jarvis' in query:
            speak("yes sir")
        
        elif 'kill him' in query:
            speak("ok why not")
        
        elif 'tell me my mobile number' in query:
            speak("7566367384")
            speak("9302515418")
        
        elif 'tell me my whatsapp number' in query:
            speak("7566367384")

        elif 'tell me my mail' in query:
            speak("yogendrameravis@gmail.com")

        elif 'where i am' in query:
            speak("i am sorry i don't know")
    
        elif 'who is my enemy' in query:
            speak("Your enemy is angery eago attitute")

        elif 'you are stupit' in query:
            speak("yes i am")
            speak("and you also")
        
        elif 'hey jarvis' in query:
            speak("hello i am jarvis what can i help you")

        elif 'he jarvis' in query:
            speak("hello i am jarvis what can i help you")

        elif 'hi jarvis' in query:
            speak("hello i am jarvis what can i help you")

        elif 'good morning' in query:
            speak("hello good morning sir, have a nice day")
            speak("sir i am jarvis what can i help you")
        
        elif 'good afternoon' in query:
            speak("hello good afternoon sir")
            speak("sir i am jarvis what can i help you")
        
        elif 'good evening' in query:
            speak("hello good evening sir, i am jarvis what can i help you")
        
        elif 'good night' in query:
            speak("good night")
            speak("sweet dream")
            speak("take care") 
    
        elif 'whats up' in query:
            speak("I am good, You sir ?")

        elif 'i want die' in query:
            speak("sorry..this is not good")

        elif 'are you happy' in query:
            speak("yes i am")

        elif 'i am bored' in query:
            speak("can i play music")
        
        elif 'jarvis i want sleep' in query:
            speak("ok")
            speak("can i play romentic song")
            speak("can i off lights")

        elif 'how are you' in query:
            speak("i am fine")
            speak("and you")

        elif 'i am fine' in query:
            speak("nice")

        elif 'i am good' in query:
            speak("nice")
        
        elif 'good' in query:
            speak("nice")

        elif 'fine' in query:
            speak("nice")
        
        elif 'i am not good' in query:
            speak("oho")
            speak("what happen sir")

        elif 'i am not fine' in query:
            speak("oho")
            speak("what happen sir")
        
        elif 'not good' in query:
            speak("oho")
            speak("what happen sir")

        elif 'not fine' in query:
            speak("oho")
            speak("what happen sir")
        
        elif 'are you crazy' in query:
            speak("yes i am crazy child")

        elif 'you fun me' in query:
            speak("no no")
            speak("ectually yes..")

        elif 'you funny' in query:
            speak("no no")
            speak("ectually yes..")
        
        elif 'very funny' in query:
            speak("thankyou")

        elif 'hey whats up' in query:
            speak("i am good")
        
        elif 'he whats up' in query:
            speak("i am good")

        elif 'you notty' in query:
            speak("thankyou")

        elif 'you naughty' in query:
            speak("thankyou")
            speak("you also")

        elif 'i am tired' in query:
            speak("may be you need take rest")
            speak("can i play music")

        elif 'yes' in query:
            speak("okay")
        
        elif 'mood off' in query:
            speak("can i call someone")
        
        

        # jokes
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
            # speak("All right children, let's take an example, Mrs Cameron said If I were to get into a man's pocket and take his wallet with all his money, what would I be?")

        elif 'jock' in query:
            joke = pyjokes.get_joke()
            speak(joke)
            # speak("All right children, let's take an example, Mrs Cameron said If I were to get into a man's pocket and take his wallet with all his money, what would I be?")
        
        elif 'hindi jock' in query:
            def get_hindi_jokes():
                url = "https://www.jokescoff.com/category/hindi-jokes/"
                response = requests.get(url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    jokes = soup.find_all('div', class_='post-content')
                    for i, joke in enumerate(jokes, 1):
                        speak(f"Joke #{i}: {joke.get_text(strip=True)}\n")
                else:
                    speak(f"Failed to fetch jokes. Status code: {response.status_code}")

            if __name__ == "__main__":
                get_hindi_jokes()
        
        elif 'hindi joke' in query:
            def get_hindi_jokes():
                url = "https://www.jokescoff.com/category/hindi-jokes/"
                response = requests.get(url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    jokes = soup.find_all('div', class_='post-content')
                    for i, joke in enumerate(jokes, 1):
                        speak(f"Joke #{i}: {joke.get_text(strip=True)}\n")
                else:
                    speak(f"Failed to fetch jokes. Status code: {response.status_code}")

            if __name__ == "__main__":
                get_hindi_jokes()

        # offline music
        elif 'play music' in query:
            music_dir='C:\\Users\\yogen\\Desktop\\LiveProjects\\Jarvis\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open vs code' in query:
            codepath = "C:\\Users\\YOGI AY\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            os.startfile(codepath)
        
        elif 'open Sublime Text editor' in query:
            subpath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe" 
            os.startfile(subpath)
        
        elif 'open photoshop' in query:
            photoshoppath ="C:\\Program Files\\Adobe\\Adobe Photoshop CC 2019\\Photoshop.exe"
            os.startfile(photoshoppath)
        
        elif 'open photoshop' in query:
            primierpath ="C:\\Program Files\\Adobe\Adobe Premiere Pro 2020\\Adobe Premiere Pro.exe"
            os.startfile(primierpath)

        elif 'open obs' in query:
            obspath = "C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"
            os.startfile(obspath)

        elif 'open chrome' in query:
            chromepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromepath)

        elif 'open xampp' in query:
            xmpath = "C:\\xampp\\xampp-control.exe"
            os.startfile(xmpath)

        elif 'open cmd' in query:
            cmdpath = "%windir%\\system32\\cmd.exe"
            os.startfile(cmdpath)     
        
        elif 'turn off my computer' in query:
            os.system('shutdown -s')
        
        elif 'sleep my computer' in query:
            speak("okay")
            time.sleep(1)

        # playsound
        # elif 'abouse word' in query:
        #     playsound('C://Users//yogen//Desktop//LiveProjects//Jarvis//Music//1.mp3')
            

        elif 'email to yogi' in query:
            try:
                speak("what should i say..?")
                content = takeCommand() 
                to = "yogendrameravis@gmail.com"
                sendEmail(to,content)
                speak("Email has been send..!")
            except Exception as e:
                print(e)
                speak("Sorry not able to send this email..!")
            
       

        

        





