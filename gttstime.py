from gtts import gTTS
import os
from datetime import datetime

def num2words(num):
	under_20 = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
	tens = ['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
	above_100 = {100: 'Hundred',1000:'Thousand', 1000000:'Million', 1000000000:'Billion'}
 
	if num < 20:
		 return under_20[num]
	
	if num < 100:
		return tens[(int)(num/10)-2] + ('' if num%10==0 else ' ' + under_20[num%10])
 
	# find the appropriate pivot - 'Million' in 3,603,550, or 'Thousand' in 603,550
	pivot = max([key for key in above_100.keys() if key <= num])
 
	return num2words((int)(num/pivot)) + ' ' + above_100[pivot] + ('' if num%pivot==0 else ' ' + num2words(num%pivot))

now = datetime.now()
dt_string = now.strftime("%H:%M:%S")
print("date and time =", dt_string)	

if int(now.strftime("%M"),10)<=30:
    if int(now.strftime("%H")) >12:
    	Ho = num2words(int(now.strftime("%H"),10)-12)
    else:
    	Ho = num2words(int(now.strftime("%H"),10))
else:
    if int(now.strftime("%H")) >12:
    	Ho = num2words(int(now.strftime("%H"),10)+1-12)
    else:
    	Ho = num2words(int(now.strftime("%H"),10)+1)


if int(now.strftime("%M"),10)> 30:
    Mi = num2words(60-int(now.strftime("%M"),10))
else:
    Mi = num2words(int(now.strftime("%M"),10))


def tellthetime():

    if int(now.strftime("%M"),10) == 0:
    	tts = gTTS("It is "+Ho+" o'clock")#, lang='ja')
    elif int(now.strftime("%M"),10) ==15:
    	tts = gTTS("It is quarter past "+Ho)#, lang='ja')
    elif int(now.strftime("%M"),10) ==30:
    	tts = gTTS("It is half past "+Ho)#, lang='ja')
    elif int(now.strftime("%M"),10) ==45:
    	tts = gTTS("It is quarter to "+Ho)#, lang='ja')
    else :
    	tts = gTTS("It is "+Ho+" , "+Mi+ "." )#, lang='ja')

    tts.save(dt_string+'.mp3')

tellthetime()
