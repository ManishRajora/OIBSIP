# VICO Voice Assistant

import datetime
import speech_recognition as sr
import pyttsx3
import urllib.parse
import webbrowser

# fxn for assistant to speak
def speak(text):
    print(f'Assistant: {text}')
    # Initialize pyttsx3 here to avoid the runAndWait loop bug
    engine = pyttsx3.init()
    engine.setProperty('rate', 165)
    engine.say(text)
    engine.runAndWait()

# fxn for voice recognition
def take_command():
    listner = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listning.....')
        listner.adjust_for_ambient_noise(source, duration=0.8)       # ignore background noises
        try:
            voice = listner.listen(source, timeout=10, phrase_time_limit=10)
            print('Processing....')
            processed_command = listner.recognize_google(voice)
            print(f'command: {processed_command}')
            return processed_command.lower()
        except sr.WaitTimeoutError:              # error if didn't say anything for 10 sec
            speak('Looks like you didn\'t speak anything, please try again.')
        except sr.UnknownValueError:             # error if couldn't understand the voice
            speak('Your instructions are unclear, please repeat that again.')
        except sr.RequestError:                  # error if network problem
            speak('Seems like you are offline, please check your internet connection.')

    return ''

# fxn for handling commands
def handle_command(command):
    # examine the command and perform specified actions
    if not command:
        return True

    if command in ['exit', 'stop', 'terminate', 'bye', 'goodbye']:
        speak('Ok, Have a great day')
        return False
    
    if command in ['hey vico', 'hello vico', 'hi vico', 'hello', 'hey', 'hi', 'greetings vico', 'wake up vico']:
        speak('Hello! I am VICO, your personal AI assistant. How can I help you today?')
    elif command == 'how are you':
        speak('I am fine, thank you for asking. How can I help you today?')
    elif command in ['what time it is', 'tell me the time', 'what is the time', 'time', 'current time']:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f'Its {current_time}')
    elif command in ['date', 'what date is it', 'tell me the date', 'today\'s date', 'current date']:
        current_date = datetime.datetime.now().strftime('%A, %B %d, %Y')
        speak(f'Today is {current_date}')
    elif command in ['help', 'list of commands', 'what can you do']:
        speak('I can only help you with a limited set of tasks, like telling date, time and searching web for now.')
    elif 'search' in command or 'search for' in command:
        query = command.replace('search', '').replace('for', '').strip()
        if query:
            speak(f'Searching web for {query}')
            search_query = urllib.parse.quote(query)
            url = f'https://www.google.com/search?q={search_query}'
            webbrowser.open(url)
        else:
            speak('What would you like to search for?')
    else:
        speak('Sorry, I can\'t assist with that request. I am still under development and can only assist with limited commands.')

    return True

        
# starting area
speak('Your Voice assistant VICO is now active.')
assistant_running = True
while assistant_running:
    input = take_command()
    if input:
        assistant_running = handle_command(input)
    
