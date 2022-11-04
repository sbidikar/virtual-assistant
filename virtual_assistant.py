import speech_recognition as sr # recognise speech
import playsound # to play an audio files
from gtts import gTTS # google text to speech
import random
import time
import datetime
import webbrowser # open browser
import os # to remove



def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def engine_speak(text):
    text = str(text)

r = sr.Recognizer() # initialise a recogniser
# listen for audio and convert it to text:
def record_audio(ask=""):
    with sr.Microphone() as source: # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            engine_speak('I did not get that')
        except sr.RequestError:
            engine_speak('Sorry, the service is down') # error: recognizer is not connected
        print(">>", voice_data.lower()) # print what user said
        return voice_data.lower()

# get string and make a audio file to be played
def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    os.remove(audio_file) # remove audio file

def respond(command):

    #name
    if there_exists(["what is your name","what's your name","tell me your name"]):
            engine_speak("My name is David")

    #greeting
    if there_exists(["how are you","how are you doing"]):
        engine_speak("I'm very well, thanks for asking ")

    # time
    if there_exists((["what","what's"] or ["tell"]) and ["time"]):
        time = str(datetime.datetime.now())
        print(time)
        hour = time[11:13]
        min = time[14:16]
        current_time = "The time is " + hour + "Hours and" + min + "Minutes"
        engine_speak(current_time)

    #search google
    if there_exists(["search for"]) and 'youtube' not in command:
        search_term = command.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + "on google")

    #search youtube
    if there_exists(["search on youtube for","youtube"]):
        search_term = command.split("for")[-1]
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + "on youtube")
    
    #search amazon
    if there_exists(["amazon"]):
        search_term = command.split("for")[-1]
        url = "https://www.amazon.com/s?k="+ search_term
        webbrowser.get().open(url)
        engine_speak("here is what i found for"+search_term + "on amazon.com")
        
    if there_exists(["walmart"]):
        search_term = command.split("for")[-1]
        url = "https://www.walmart.com/search?q="+ search_term
        webbrowser.get().open(url)
        engine_speak("here is what i found for "+search_term + " on walmart.com")
    
    if there_exists(["exit", "quit", "goodbye","end"]):
        engine_speak("GoodByee")
        exit()
        


time.sleep(1)
voice_data = record_audio("Hi I am david your virtual assistant")
while(1):
    voice_data = record_audio("") # get the voice input
    print("Done")
    print("Q:", voice_data)
    if voice_data.startswith('hey david'):
        print('listening')
        command = voice_data.split('hey david ')[-1]
        if command == 'hey david':
            greetings = ["hey, how can I help you", "hey, what's up?", "I'm listening", "how can I help you?", "hello"]
            greet = greetings[random.randint(0,len(greetings)-1)]
            engine_speak(greet)
        else:
            print(command)
            respond(command) # respond
