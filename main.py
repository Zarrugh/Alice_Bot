import internetConState
import gtts
import speech_recognition as sr
import sys
import signal
import GetFromJeson
import filter
import send_to_wit
import TxTV
import os
import subprocess
import vlc
import _thread as thread
import time
import GetFWolfranalpha
import random

from playsound import playsound
from snowboy import snowboydecoder
from datetime import datetime
from wit import Wit

offline_detector_state = False

player = vlc.MediaPlayer("/home/zarrugh/Music/01. Detective Conan Main Theme.flac")

def ubdate_info():
    if internetConState.internet_on():
        print("geting data")
    print("Done")
    time.sleep(58)
DGC =0
def Main_detected_callback():
    global offline_detector_state
    global DGC
    print ("hotword detected")
    if internetConState.internet_on():
        FilteredResp={}
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Please say something")
            audio = r.listen(source)
            print("Recognizing Now .... ")
            try:
                wit_resp={}
                WBS= r.recognize_google(audio)
                print(WBS)
                wit_resp=send_to_wit.send(WBS)
                print(wit_resp)
                FilteredResp=filter.filter_resp(wit_resp)
            except Exception as e:
                print("Error :  " + str(e))
            print(FilteredResp)
        if 'intents' in FilteredResp :
            if FilteredResp['intents'][0] == 'greeting' or FilteredResp['intents'][0] == 'Ggreeting' :
                try:
                    x=random.randrange(1, 4)
                    playsound("Phasor/G"+str(x)+".mp3")
                except Exception as e:
                    TxTV.TXT()
                    playsound("Phasor/G"+str(x)+".mp3")
                DGC =0

            elif FilteredResp['intents'][0] == 'Qgreeting':
                try:
                    x=random.randrange(1, 4)
                    playsound("Phasor/Q"+str(x)+".mp3")
                except Exception as e:
                    TxTV.TXT()
                    playsound("Phasor/Q"+str(x)+".mp3")
                DGC =0

            elif FilteredResp['intents'][0] == 'ask_time':
                Time_detected_callback()
                DGC =0

            elif FilteredResp['intents'][0] == 'ask_weather':
                WARes=GetFWolfranalpha.geting_from_wolframalpha(WBS)
                try:
                    tts = gtts.gTTS(WARes)
                    tts.save("temp.mp3")
                    playsound("temp.mp3")
                except Exception as e:
                    print("Error :  " + str(e))
                DGC = 0

            elif FilteredResp['intents'][0] == 'asking_for_help':
                try:
                    playsound("Phasor/HCIHY.mp3")
                except Exception as e:
                    TxTV.TXT()
                    playsound("Phasor/HCIHY.mp3")
                DGC = 0

            elif FilteredResp['intents'][0] == 'open_app':
                if 'entities' in FilteredResp :
                    try:
                        tts = gtts.gTTS("openning "+FilteredResp['entities']['appTopen'])
                        print("gtts.gTTS(openning +FilteredResp['entities'][1])")
                        tts.save("temp.mp3")
                        playsound("temp.mp3")
                    except Exception as e:
                        print("Error :  " + str(e))
                    try:
                        subprocess.Popen([FilteredResp['entities']['appTopen']])
                    except Exception as e:
                        print("Error: "+str(e))
                        try:
                            playsound("Phasor/ICFIAWTN.mp3")
                        except Exception as e:
                            TxTV.TXT()
                            playsound("Phasor/ICFIAWTN.mp3")
                    DGC =0
                else:
                    try:
                        playsound("Phasor/ICFOWATO.mp3")
                    except Exception as e:
                        TxTV.TXT()
                        playsound("Phasor/ICFOWATO.mp3")
                    DGC =0

            elif FilteredResp['intents'][0] == 'open_door':
                if 'entities' in FilteredResp :
                    try:
                        tts = gtts.gTTS("unlocking "+FilteredResp['entities']['doors'])
                        tts.save("temp.mp3")
                        playsound("temp.mp3")
                    except Exception as e:
                        print("Error :  " + str(e))
                    DGC =0
                else:
                    try:
                        playsound("Phasor/ICFOWDTUL.mp3")
                    except Exception as e:
                        TxTV.TXT()
                        playsound("Phasor/ICFOWDTUL.mp3")
                    DGC =0

            elif FilteredResp['intents'][0] == 'close_door':
                if 'entities' in FilteredResp :
                    try:
                        tts = gtts.gTTS("locking "+FilteredResp['entities']['doors'])
                        tts.save("temp.mp3")
                        playsound("temp.mp3")
                    except Exception as e:
                        print("Error :  " + str(e))
                    DGC =0
                else:
                    try:
                        playsound("Phasor/ICFOWDTL.mp3")
                    except Exception as e:
                        TxTV.TXT()
                        playsound("Phasor/ICFOWDTL.mp3")
                    DGC =0

            elif FilteredResp['intents'][0] == 'turn_off':
                if 'entities' in FilteredResp :
                    try:
                        tts = gtts.gTTS("turning off "+FilteredResp['entities']['turn_object'])
                        tts.save("temp.mp3")
                        playsound("temp.mp3")
                    except Exception as e:
                        print("Error :  " + str(e))
                    DGC =0
                else:
                    try:
                        playsound("Phasor/ICFOWOTT.mp3")
                    except Exception as e:
                        TxTV.TXT()
                        playsound("Phasor/ICFOWOTT.mp3")
                    DGC =0

            elif FilteredResp['intents'][0] == 'turn_on':
                if 'entities' in FilteredResp :
                    try:
                        tts = gtts.gTTS("turning on "+FilteredResp['entities']['turn_object'])
                        tts.save("temp.mp3")
                        playsound("temp.mp3")
                    except Exception as e:
                        print("Error :  " + str(e))
                    DGC =0
                else:
                    try:
                        playsound("Phasor/ICFOWOTT.mp3")
                    except Exception as e:
                        TxTV.TXT()
                        playsound("Phasor/ICFOWOTT.mp3")
                    DGC =0

            elif FilteredResp['intents'][0] == 'who_search' or FilteredResp['intents'][0] == 'wolframalpha':
                WARes=GetFWolfranalpha.geting_from_wolframalpha(WBS)
                print("WARes")
                try :
                    tts = gtts.gTTS(WARes)
                    tts.save("temp.mp3")
                except Exception as e :
                    print("error :"+ str(e))
                playsound("temp.mp3")
                DGC =0
        else:
            if DGC < 3:
                try:
                    playsound("Phasor/SIDGTCYRP.mp3")
                except Exception as e:
                    TxTV.TXT()
                    playsound("Phasor/SIDGTCYRP.mp3")
                DGC +=1
                Main_detected_callback()
            else:
                try:
                    playsound("Phasor/SIDGTCYRP.mp3")   #*/-*/*-56465
                except Exception as e:
                    TxTV.TXT()
                    playsound("Phasor/SIDGTCYRP.mp3")
                    DGC=0

    else:
        print("offline mode")
        offline_detector.start(detected)
        offline_detector_state=True

def Light_On_detected_callback():
    global offline_detector_state
    LNURL="https://api.thingspeak.com/update?api_key=SI67Y3B0F5VEWTY5&field1=1"
    print("Light_On_detected_callback")
    if offline_detector_state :
        offline_detector.terminate()
        offline_detector_state=False
    return()

def Light_Off_detected_callback():
    global offline_detector_state
    LFURL="https://api.thingspeak.com/update?api_key=SI67Y3B0F5VEWTY5&field1=0"
    print("Light_Off_detected_callback")

    if offline_detector_state :
        offline_detector.terminate()
        offline_detector_state=False
    return()

def Time_detected_callback():
    global offline_detector_state
    now = datetime.now()
    M=now.strftime("%M")
    H=now.strftime("%H")
    print("H = "+H+" , M ="+ M)
    if int(H) >12:
        H=int(H)-12
        H="0"+str(H)
    try:
        playsound("Time/"+str(H)+":"+str(M)+".mp3")
    except Exception as e:
        print(e)
    if offline_detector_state :
        offline_detector.terminate()
        offline_detector_state=False
    return()

def Temp_detected_callback(IntState):
    global offline_detector_state
    if IntState:

        try:
            temp_url = "https://api.thingspeak.com/channels/471406/feeds.json?results=2"
            temp = geting_from_jurl_TSVer(temp_url)
            tts = gTTS("the temperature is "+ temp +" celsius.")
            tts.save('temp.mp3')
        except Exception as e:
            print("Erorr: "+str(e))
    else:
        print("NO internet")
    if offline_detector_state :
        offline_detector.terminate()
        offline_detector_state=False
    return()

def Play_Pause():
    os.popen('xdotool key XF86AudioPlay')
    return()

def Previous():
    os.popen('xdotool key XF86AudioPrev')
    return()
def Next():
    os.popen('xdotool key XF86AudioNext')
    return()
def volume_down():
    os.popen('xdotool key XF86AudioLowerVolume')
    return()

def volume_up():
    os.popen('xdotool key XF86AudioRaiseVolume')
    return()

def volume_Mute():
    os.popen('xdotool key XF86AudioMute')
    return()

def What_to_say_detected_callback():
    global offline_detector_state
    print("What_to_say_detected_callback")
    if offline_detector_state :
        offline_detector.terminate()
        offline_detector_state=False
    return()

def Weather_detected_callback():
    global offline_detector_state
    print("Weather_detected_callback")
    if offline_detector_state :
        offline_detector.terminate()
        offline_detector_state=False
    return()


def Volume_Up_detected_callback():
    global offline_detector_state
    print("Volume_Up_detected_callback")
    if offline_detector_state :
        offline_detector.terminate()
        offline_detector_state=False
    return()


def Volume_Down_detected_callback():
    global offline_detector_state
    print("Volume_Down_detected_callback")
    if offline_detector_state :
        offline_detector.terminate()
        offline_detector_state=False
    return()


def print_time( threadName, delay):
   count = 0
   while count < 100:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

try:
    wit_access_token="AE65KEMFT5PBOQZ6ZDSQJIMUY33L4BQE"
    wit_client = Wit(wit_access_token)
except Exception as e:
    print("Wit Error :  " + str(e))

#thread.start_new_thread( print_time, ("Thread-1", 59, ) )
#thread.start_new_thread(ubdate_info,())
detected = [Light_On_detected_callback,Light_Off_detected_callback,Time_detected_callback,
            Temp_detected_callback,Play_Pause,Next,What_to_say_detected_callback,
	    Weather_detected_callback,Volume_Up_detected_callback,Volume_Down_detected_callback]
OfflineHotWord=["pmdl/Turn_The_Light_On.pmdl","pmdl/Turn_Off_The_Light.pmdl","pmdl/WhatsTheTime.pmdl","pmdl/what's_the_temp.pmdl","pmdl/stop_playing_music.pmdl",
                "pmdl/play_music.pmdl","pmdl/what_can_i_say.pmdl","pmdl/what's_the_weather.pmdl","pmdl/turn_up_the_volume.pmdl","pmdl/turn_down_the_volume.pmdl"]
Alice_detector = snowboydecoder.HotwordDetector("pmdl/hey_alice.pmdl",sensitivity = 0.5, audio_gain = 1)
offline_detector = snowboydecoder.HotwordDetector(OfflineHotWord,sensitivity = 0.5, audio_gain = 1)
Alice_detector.start(Main_detected_callback)
