# Voice Assistant Vico - Techincal documentation and code breakdown

## Library used
- `speech_recognition` - take input voice and send it to recognition services to convert into text
- `pyttsx3` - convert text into speech
- `urllib.parse` - manipulate the search query into valid web format
- `webbrowser` - open default web browser
- `datetime` - used to get current date and time

## Function breakdown
- `speak(text)`
    - convert string into audio and speak with output in terminal
        - intialized pyttsx3 engine inside the fxn locally to avoid the runAndWait loop bug causes it to get skipped after first initialization.
        - `engine.setProperty()` - set the rate of speech
        - `engine.say()` - queue the text to be spoken
        - `engine.runAndWait()` - block until all queued speech is complete and release the resources 

- `take_command()`
    - take the user's audio using microphone and convert it into lowercase string
        - `listner = sr.Recognizer()` - intialize recognizer
        - `listner.adjust_for_ambient_noise()` - adjust for background noises
        - `listner.listen()` - listen to the audio with a 10 sec recording limit and 10 sec timeout
        - `listner.recognize_google()` - recognize the audio using google's speech recognition
        - handles errors like `sr.WaitTimeoutError`, `sr.UnknownValueError`, `sr.RequestError` and print appropriate messages

- `handle_command(command)`
    - compare the command and perform specified actions
        - checks for the following commands and performs the corresponding actions:
            - 'exit', 'stop', 'terminate', 'bye', 'goodbye' - exit the program
            - 'hey vico', 'hello vico', 'hi vico', 'hello', 'hey', 'hi', 'greetings vico', 'wake up vico' - greet the user
            - 'how are you' - respond to the user's question
            - 'what time it is', 'tell me the time', 'what is the time', 'time', 'current time' - tell the current time
            - 'date', 'what date is it', 'tell me the date', 'today\'s date', 'current date' - tell the current date
            - 'help', 'list of commands', 'what can you do' - list the available commands
            - 'search' or 'search for' - search the web for the specified query
            - else - print and speak the error message