import speech_recognition as sr

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
    except Exception as e:
        print("Error :  " + str(e))

# recognize_bing
# recognize_google
# recognize_google_cloud
# recognize_houndify
# recognize_ibm
# recognize_wit
