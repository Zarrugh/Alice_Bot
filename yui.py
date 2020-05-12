from snowboy import snowboydecoder 
def detected_callback(): 
    print ("hotword 1 detected")

def detected_callback1(): 
    print ("hotword 2 detected")
	
models=["Hey_Yui.pmdl","Alexa.pmdl"]
	# do your task here or call other program. 
detector = snowboydecoder.HotwordDetector(models, 
					sensitivity = 0.5, audio_gain = 1) 

detector.start([detected_callback,detected_callback1]) 
