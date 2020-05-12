form snowboy import snowboydecoder
import sys
import signal
interrupted = False
def signal_handler(signal, frame):
    global interrupted
    interrupted = True
def interrupt_callback():
    global interrupted
    return interrupted
if len(sys.argv) != 3:
    print("Usage: python demo.py 1st.model 2nd.model")
    print("Error: need to specify 2 model names")
    sys.exit(-1)
models = sys.argv[1:]
print(models)
signal.signal(signal.SIGINT, signal_handler)
sensitivity = [0.5]*len(models)
detector = snowboydecoder.HotwordDetector(models, sensitivity=sensitivity)
callbacks = [lambda: snowboydecoder.play_audio_file(snowboydecoder.DETECT_DING),
             lambda: snowboydecoder.play_audio_file(snowboydecoder.DETECT_DONG)]
print('Listening... Press Ctrl+C to exit')
detector.start(detected_callback=callbacks,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)
detector.terminate()
