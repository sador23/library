from gtts import gTTS
import subprocess
import vlc
import speech_recognition
import os
from commands import Commands

class voiceRec:
    recognizer = speech_recognition.Recognizer()
    def __init__(self,gui):
        self.gui=gui


    def read(self):
        with speech_recognition.Microphone() as source:
            voiceRec.recognizer.adjust_for_ambient_noise(source)
            audio = voiceRec.recognizer.listen(source)
        return voiceRec.recognizer.recognize_google(audio)


    def startup(self):
        audio_file="hi.mp3"
        tts=gTTS(text="Welcome sir, how may I be of assistance?",lang="en")
        tts.save(audio_file)
        p=vlc.MediaPlayer("hi.mp3")
        p.play()
        #os.remove("hi.mp3")

    def recognize(self,text):
        if text in ["login","plugin","logging","log","log-in","logging-in","plug-in"] :
            self.login_screen()
        if text.lower() in ["username","user name", "user","name","use a name","use of name","user-name","use-of-a-name","use-a-name"]:
            self.user_name_enter()

    def login_screen(self):
        audio_file="hi.mp3"
        tts=gTTS(text="Login selected, now logging in",lang="en")
        tts.save(audio_file)
        p=vlc.MediaPlayer("hi.mp3")
        Commands.login()
        print("login")
        p.play()
        #os.remove("hi.mp3")

    def user_name_enter(self):
        audio_file="hi.mp3"
        tts=gTTS(text="Username Selected, please enter username",lang="en")
        tts.save(audio_file)
        print("username")
        p=vlc.MediaPlayer("hi.mp3")
        p.play()
        #os.remove("hi.mp3")

    def main(self):
        self.startup()
        while True:
            x=self.read()
            print(x)
            self.recognize(x)
