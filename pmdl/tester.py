from snowboy import snowboydecoder
def Main_detected_callback(): 
    print ("hotword detected") 
Yui_detector = snowboydecoder.HotwordDetector("what's_the_weather.pmdl",sensitivity = 0.5, audio_gain = 1) 
Yui_detector.start(Main_detected_callback)

