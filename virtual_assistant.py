import speech_recognition as sr # recognise speech
import playsound # to play an audio files
from gtts import gTTS # google text to speech
import random
import time
import webbrowser # open browser
import os # to remove 
import bs4 as bs



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

def respond(voice_data):
    # 1: greeting
    if there_exists(['hey','hi','hello']):
        greetings = ["hey, how can I help you", "hey, what's up?", "I'm listening", "how can I help you?", "hello"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        engine_speak(greet)

    # 2: name
    if there_exists(["what is your name","what's your name","tell me your name"]):
            engine_speak("My name is Karen")

    # 3: greeting
    if there_exists(["how are you","how are you doing"]):
        engine_speak("I'm very well, thanks for asking ")

    # 4: time
    if there_exists((["what","what's"] or ["tell"]) and ["time"]):
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        engine_speak(current_time)

    # 5: search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + "on google")

    # 6: search youtube
    if there_exists(["search on youtube for","youtube"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + "on youtube")
    
    # 6: search amazon
    if there_exists(["amazon"]):
        search_term = voice_data.split("for")[-1]
        webbrowser.get().open(url)
        engine_speak("here is what i found for"+search_term + "on amazon.com")
    
    if there_exists(["exit", "quit", "goodbye","end"]):
        engine_speak("GoodByee")
        exit()
        


time.sleep(1)

voice_data = record_audio("Hi I am Karen your virtual assistant")
while(1):
    voice_data = record_audio("") # get the voice input
    print("Done")
    print("Q:", voice_data)
    respond(voice_data) # respond
