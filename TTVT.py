import pyglet
from playsound import playsound
import pygame, time
import tempfile
from gtts import gTTS
from pygame import mixer
from tempfile import TemporaryFile
mixer.init()

tts = gTTS("the temperature is -21 celsius.")
'''
tts.save("try.mp3")
playsound("try.mp3")
'''

sf = TemporaryFile()
tts.write_to_fp(sf)
sf.seek(0)
mixer.music.load(sf)
mixer.music.play()

tts = gTTS("the temperature is 21 celsius.")
'''
tts.save("try.mp3")
playsound("try.mp3")
'''

sf = TemporaryFile()
tts.write_to_fp(sf)
sf.seek(0)
mixer.music.load(sf)
mixer.music.play()

