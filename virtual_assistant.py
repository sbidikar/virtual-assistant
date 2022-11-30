import speech_recognition as sr # recognise speech
import pyttsx3
import playsound # to play an audio files
from gtts import gTTS # google text to speech
import random
import time
import datetime
import webbrowser # open browser
import os # to remove
import wikipedia



def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def engine_speak(text):
    text = str(text)

r = sr.Recognizer() # initialise a recogniser
engine = pyttsx3.init()
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
            engine_speak('I did not get that, please say with Hi David')
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
    if there_exists(["time"]):
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        current_time = "The time is " + time
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
    
    if there_exists(["who is"]):
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        engine_speak(info)
        if there_exists(["game"]):
            voice_data = record_audio("choose among rock paper or scissor")
        moves=["rock", "paper", "scissor"]
    
        cmove=random.choice(moves)
        pmove=voice_data
        

        engine_speak("The computer chose " + cmove)
        engine_speak("You chose " + pmove)
        #engine_speak("hi")
        if pmove==cmove:
            engine_speak("the match is draw")
        elif pmove== "rock" and cmove== "scissor":
            engine_speak("Player wins")
        elif pmove== "rock" and cmove== "paper":
            engine_speak("Computer wins")
        elif pmove== "paper" and cmove== "rock":
            engine_speak("Player wins")
        elif pmove== "paper" and cmove== "scissor":
            engine_speak("Computer wins")
        elif pmove== "scissor" and cmove== "paper":
            engine_speak("Player wins")
        elif pmove== "scissor" and cmove== "rock":
            engine_speak("Computer wins")

    #11 toss a coin
    if there_exists(["toss","flip","coin"]):
        moves=["head", "tails"]   
        cmove=random.choice(moves)
        engine_speak("The computer chose " + cmove)
    
        #12 calc
    if there_exists(["plus","minus","multiply","divide","power","+","-","*","/"]):
        opr = voice_data.split()[1]

        if opr == '+':
            engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-':
            engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'multiply':
            engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'divide':
            engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == 'power':
            engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            engine_speak("Wrong Operator")
    
    if there_exists(["exit", "quit", "goodbye","end"]):
        engine_speak("GoodByee")
        exit()
        


time.sleep(1)
voice_data = record_audio("Hi I am david your virtual assistant, you can ask me anything by saying Hi David")
while(1):
    voice_data = record_audio("") # get the voice input
    print("Done")
    print("Q:", voice_data)
    if voice_data.startswith('hey david') or voice_data.startswith('hi david') :
        print('listening')
        command = voice_data.split('david ')[-1]
        print('command '+ command)
        if command == ('hey david' or 'hi david'):
            greetings = ["hey, how can I help you", "hey, what's up?", "I'm listening", "how can I help you?", "hello"]
            greet = greetings[random.randint(0,len(greetings)-1)]
            engine_speak(greet)
        else:
            print(command)
            respond(command) # respond
