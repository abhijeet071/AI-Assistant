import requests
import pyttsx3
import speech_recognition as sr
from decouple import config
from datetime import datetime
from functions.task_automation import set_reminder, add_todo, get_todo_list
from random import choice

from functions.online_ops import (
    find_my_ip, get_latest_news, get_random_advice, get_random_joke,
    get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia,
    send_email, send_whatsapp_message
)
from functions.os_ops import open_calculator, open_camera, open_cmd, open_notepad
from utils import opening_text
from random import choice
from functions.nlp_processing import recognize_intent 
from functions.task_automation import set_reminder, add_todo, get_todo_list

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('sapi5')

engine.setProperty('rate', 190)
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    """Speaks the given text"""
    engine.say(text)
    engine.runAndWait()

def greet_user():
    """Greets the user based on the time of day"""
    hour = datetime.now().hour
    if 6 <= hour < 12:
        speak(f"Good Morning {USERNAME}")
    elif 12 <= hour < 16:
        speak(f"Good Afternoon {USERNAME}")
    elif 16 <= hour < 19:
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")



def take_user_input():
    """Listens for user input and converts speech to text or allows typing"""
    choice = input("Press 'S' for Speak, 'T' for Type: ").strip().lower()
    
    if choice == 's':
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening....')
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query.lower()
        except Exception:
            speak('Sorry, I could not understand. Could you please say that again?')
            return None

    elif choice == 't':
        query = input("Type your query: ").strip().lower()
        print(f"Typed Query: {query}")
        return query

    else:
        print("Invalid choice! Please press 'S' or 'T'.")
        return take_user_input()





def get_latest_news():
    url = "https://api.thenewsapi.com/v1/news/top?api_token=95hvFRwZ5ZLqjGdCm6WeBnHrGUoIEQCSN85vfKKG&locale=in"
    response = requests.get(url)
    data = response.json()
    return [article["title"] for article in data.get("data", [])][:10]






def execute_command(query):
    """Executes commands based on the recognized intent"""
    if not query:
        return

    intent = recognize_intent(query)

    speak(choice(opening_text))

    if intent == "open_notepad":
        speak("Opening Notepad.")
        open_notepad()

    elif intent == "open_cmd":
        speak("Opening Command Prompt.")
        open_cmd()

    elif intent == "open_camera":
        speak("Opening Camera.")
        open_camera()

    elif intent == "open_calculator":
        speak("Opening Calculator.")
        open_calculator()

    elif intent == "weather":
        try:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text.strip()
            if not city:
                speak("Sorry, I couldn't detect your city. Please try again.")
            else:
                speak(f"Getting weather report for {city}...")
                weather_data = get_weather_report(city)

            if weather_data:
                weather, temperature, feels_like = weather_data 

                speak(f"The current temperature in {city} is {temperature}, but it feels like {feels_like}.")
                speak(f"The weather report mentions {weather}.")
                
                print(f"City: {city}\nWeather: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
            else:
                speak("Sorry, I couldn't fetch the weather details at the moment.")
        except Exception as e:
            print("Error fetching weather:", e)
            speak("Sorry, I couldn't fetch the weather details. Please try again later.")


    elif intent == "wikipedia":
        speak('What do you want to search on Wikipedia?')
        search_query = take_user_input()
        if search_query:
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            print(results)

    elif intent =='find_ip':
        ip_address = find_my_ip()
        speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
        print(f'Your IP Address is {ip_address}')

    elif intent == "google":
        speak('What do you want to search on Google?')
        search_query = take_user_input()
        if search_query:
            search_on_google(search_query)

    elif intent == "youtube":
        speak('What do you want to play on YouTube?')
        video = take_user_input()
        if video:
            play_on_youtube(video)

    elif intent == "news":
        speak("Fetching the latest news headlines.")
        news = get_latest_news()
        speak(news)
        print("\n".join(news))

    elif intent == "joke":
        joke = get_random_joke()
        speak(joke)
        print(joke)

    elif intent == "advice":
        advice = get_random_advice()
        speak(advice)
        print(advice)

    elif intent == "send_whatsapp":
        speak("Please enter the phone number in the console.")
        number = input("Enter the number: ")
        speak("What is the message?")
        message = take_user_input()
        if message:
            send_whatsapp_message(number, message)
            speak("Message sent successfully.")

    elif intent == "send_email":
        speak("Enter the recipient's email in the console.")
        receiver_address = input("Enter email address: ")
        speak("What is the subject?")
        subject = take_user_input()
        speak("What is the message?")
        message = take_user_input()
        if message:
            if send_email(receiver_address, subject, message):
                speak("Email sent successfully.")
            else:
                speak("Something went wrong while sending the email.")

    elif intent == "set_reminder":
        speak("What should I remind you about?")
        task = take_user_input()
    
        if task:
            speak("In how many minutes?")
            try:
                reminder_time = int(take_user_input())
                response = set_reminder(task, reminder_time)
                speak(response)
                print(response)
            except ValueError:
                speak("Sorry, I didn't understand the time. Please say a number.")

    elif intent == "add_todo":
        speak("What task should I add to your to-do list?")
        task = take_user_input()
    
        if task:
            response = add_todo(task)
            speak(response)
            print(response)

    elif intent == "show_todo":
        response = get_todo_list()
        speak(response)
        print(response)


    else:
        speak("Sorry, I didn't understand that command.")

    

if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input()
        if query in ["exit", "stop", "quit", "bye"]:
            speak("Goodbye!")
            break
        execute_command(query)
