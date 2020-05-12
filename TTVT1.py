'''import pyttsx3
engine = pyttsx3.init()
engine.setProperty('voice', 'english-us')
engine.setProperty('rate',170)  #120 words per minute
engine.setProperty('volume',1)
engine.say("the temperature is -21 celsius.")
engine.runAndWait()
'''
'''
import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
'''
import wave
try:
    from StringIO import StringIO
except ImportError:
    import io
from picotts import PicoTTS
picotts = PicoTTS()
wavs = picotts.synth_wav("Hello World!")
wav = wave.open(io.BytesIO(wavs))
wav.getnchannels(), wav.getframerate(), wav.getnframes()
wav.open()

#pico2wave( -l=en-US, -w=file.wav, "This is a test of pico")
