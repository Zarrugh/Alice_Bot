from gtts import gTTS
import os
from datetime import datetime

def num2words(num):
        under_20 = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
        tens = ['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        if num < 20:
                 return under_20[num]
        if num < 100:
                return tens[(int)(num/10)-2] + ('' if num%10==0 else ' ' + under_20[num%10])
        return num2words((int)(num/pivot)) + ' ' + above_100[pivot] + ('' if num%pivot==0 else ' ' + num2words(num%pivot))


def tellthetime(H,M):

    if H==0:
        if int(M) == 0:
            Ho = num2words(int(H))
            tts = gTTS("It is midnight")
        elif int(M) == 1:
            Ho = num2words(int(H))
            tts = gTTS("It is a minute after midnight")
        elif int(M) ==15:
            Ho = num2words(int(H))
            tts = gTTS("It is quarter past midnight")
        elif int(M) ==30:
            Ho = num2words(int(H))
            tts = gTTS("It is half past midnitght")
        elif int(M) ==45:
            Ho = num2words(int(H)+1)
            tts = gTTS("It is quarter to one")
        else :
            Ho = num2words(int(H))
            Mi = num2words(int(M))
            tts = gTTS("It is "+str(Mi)+ " minutes after midnight." )
    else:

        if int(M) == 0:
            Ho = num2words(int(H))
            tts = gTTS("It is "+str(Ho)+" o'clock")
        elif int(M) ==15:
            Ho = num2words(int(H))
            tts = gTTS("It is quarter past "+str(Ho))
        elif int(M) ==30:
            Ho = num2words(int(H))
            tts = gTTS("It is half past "+str(Ho))
        elif int(M) ==45:
            Ho = num2words(int(H)+1)
            tts = gTTS("It is quarter to "+str(Ho))
        else :
            Ho = num2words(int(H))
            Mi = num2words(int(M))
            tts = gTTS("It is "+str(Ho)+" , "+str(Mi)+ "." )

    if (int(H)<10 or int(M)<10):
        if (int(H)<10 and int(M)<10):
            if (int(M)==0 and int(H)==0):
                #print("(M==0 & H==0)")
                Name="00"+":"+"00"+".mp3"
            elif (int(M)==0):
                #print("(M==0)")
                Name="0{}:00.mp3".format(H)
            elif (int(H)==0):
                #print("(H==0)")
                Name="00:0{}.mp3".format(M)
            else:
                #print("(M!=0 & H!=0)")
                Name="0{}:0{}.mp3".format(H,M)
        elif (int(H)<10):
            if (int(H)==0):
                #print("(H==0 & M>=10)")
                Name="00:{}.mp3".format(M)
            else:
                #print("(H<10 & M>=10)")
                Name="0{}:{}.mp3".format(H,M)
        elif (int(M)<10):
            if (int(M)==0):
                #print("(M==0 & H>=10)")
                Name="{}:00.mp3".format(H)
            else:
                #print("(M<10 & H>=10)")
                Name="{}:0{}.mp3".format(H,M)
    else:
        Name="{}:{}.mp3".format(H,M)
    #print("file name : "+Name)
    tts.save("Time/"+Name)
    return
def start():
    MS = 00
    HS = 00
    MF=MS
    HF=HS
    MS=MS+1

    while (not(MS == MF and HF ==HS)):
        tellthetime(HS,MS)
        if int(MS)<59:
            MS=MS+1
        elif int(HS)<13:
            HS=int(HS+1)
            MS=int(00)
        else:
            HS=int(00)
            MS=int(00)
    return()
