import speech_recognition as sr
# from listener import Listener
from gtts import gTTS
import playsound
import os

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def speakText(text, lan):
    '''
    This function read text and save the text in
    mp3 audio to reproduce it.
    '''
    filename = 'voice.mp3'
    gtts = gTTS(text=text, lang=lan)
    gtts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def listenVoice():
    '''
    This function invoque the speech_recognition features to process
    whatever what is listened to text.
    '''
    with microphone as source:
        print('Speak anything: ')
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            return text
        except:
            print('Sorry, could not recognize your voice!')

def listenAndSpeak():
    text = listenVoice()
    speakText(text, 'en')
