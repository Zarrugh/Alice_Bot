import internetConState
from snowboy import snowboydecoder 
import speech_recognition as sr
import sys
import signal
import GetFromJeson
import os
from datetime import datetime
import subprocess
import vlc
import _thread as thread
player = vlc.MediaPlayer("/home/zaroug/Music")

def ubdate_info():
    if internetConState.internet_on():
        
    print("Done")

def play_mp3(path):
    print(path)
    subprocess.Popen(['mpg123', '-q', path]).wait()

    
def Main_detected_callback(): 
    print ("hotword detected") 
    if internetConState.internet_on():
        r = sr.Recognizer() 
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source) 
            print("Please say something") 
            audio = r.listen(source) 
            print("Recognizing Now .... ") 
            try:
                WBS= r.recognize_google(audio)
                print("WBS = " + str(WBS) + "." )
                print("Audio Recorded Successfully \n ") 
            except Exception as e:
                print("Error :  " + str(e)) 
            
    else:
        offline_detector.start(detected)
        

def Light_On_detected_callback(): 
    LNURL="https://api.thingspeak.com/update?api_key=SI67Y3B0F5VEWTY5&field1=1"
    print("Light_On_detected_callback")
    offline_detector.terminate()
    return()

def Light_Off_detected_callback(): 
    LFURL="https://api.thingspeak.com/update?api_key=SI67Y3B0F5VEWTY5&field1=0"
    print("Light_Off_detected_callback")
    offline_detector.terminate()
    return()

def Time_detected_callback():
    now = datetime.now()
    M=now.strftime("%M")
    H=now.strftime("%H")
    print("H = "+H+" , M ="+ M)
    if int(H) >12:
        H=int(H)-12
        H="0"+str(H)
    play_mp3("Time/"+str(H)+":"+str(M)+".mp3")
    offline_detector.terminate()
    return()

def Temp_detected_callback():
    try:
        temp_url = "https://api.thingspeak.com/channels/471406/feeds.json?results=2"
        temp = geting_from_jurl_TSVer(temp_url)
        tts = gTTS("the temperature is "+ temp +" celsius.")
        tts.save('temp.mp3')
    except:
        print("NO internet")
    offline_detector.terminate()
    return()
    
def Play_Music_detected_callback():
    print("Play_Music_detected_callback")
    player.play()
    offline_detector.terminate()
    return()

def Stop_Music_detected_callback():
    print("Stop_Music_detected_callback")
    player.pause()
    offline_detector.terminate()
    return()

def What_to_say_detected_callback():
    print("What_to_say_detected_callback")
    offline_detector.terminate()
    return()

def Weather_detected_callback():
    print("Weather_detected_callback")
    offline_detector.terminate()
    return()


def Volume_Up_detected_callback():
    print("Volume_Up_detected_callback")
    offline_detector.terminate()
    return()


def Volume_Down_detected_callback():
    print("Volume_Down_detected_callback")
    offline_detector.terminate()
    return()


def Mute_detected_callback():
    print("Mute_detected_callback")
    offline_detector.terminate()
    return()


def Max_detected_callback():
    print("Max_detected_callback")
    offline_detector.terminate()
    return()

thread.start_new_thread(ubdate_info())

detected = [Light_On_detected_callback,Light_Off_detected_callback,Time_detected_callback,
            Temp_detected_callback,Play_Music_detected_callback,Stop_Music_detected_callback,What_to_say_detected_callback,
	    Weather_detected_callback]#,Volume_Up_detected_callback,Volume_Down_detected_callback,Mute_detected_callback,Max_detected_callback]
OfflineHotWord=["pmdl/Turn_The_Light_On.pmdl","pmdl/Turn_On_The_Light.pmdl","pmdl/WhatsTheTime.pmdl","pmdl/what's_the_temp.pmdl","pmdl/play_music.pmdl",
                "pmdl/stop_playing_music.pmdl","pmdl/what_can_i_say.pmdl","pmdl/what's_the_weather.pmdl"]#,"pmdl/turn_up_the_volume.pmdl","pmdl/turn_down_the_volume.pmdl",
		#"pmdl/mute_the_volume.pmdl","pmdl/max_the_volume.pmdl"]'''
Yui_detector = snowboydecoder.HotwordDetector("pmdl/Hey_Yui.pmdl",sensitivity = 0.5, audio_gain = 1) 
offline_detector = snowboydecoder.HotwordDetector(OfflineHotWord,sensitivity = 0.5, audio_gain = 1) 
Yui_detector.start(Main_detected_callback)
