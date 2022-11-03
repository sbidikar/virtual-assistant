import speech_recognition as sr # recognise speech
import playsound
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

# listen for audio and convert it to text:
def record_audio(ask=""):
    with sr.Microphone() as source:
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Done Listening")
        
# get string and make a audio file to be played
def engine_speak(audio_string):
    audio_string = str(audio_string)
    
        
while(1):
    voice_data = record_audio("Recording") # get the voice input
    print("Done")
    print("Q:", voice_data)