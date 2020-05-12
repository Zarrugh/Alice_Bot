import requests
def geting_from_jurl_TSVer(jurl):
    r = requests.get(url)
    strx=str(r.json())
    strxlen=len(strx)
    while (str(strx[int(strxlen)-1]) != ":"):
        strxlen-=1
    newstex=""
    for a in strx[strxlen:]:
        if a == "." or a.isnumeric() or a=="-":
            newstex=newstex+a
    return round(float(newstex))

#url = "https://api.thingspeak.com/channels/471406/feeds.json?results=2"
#x = geting_from_jurl_TSVer(url)
#print(x)
