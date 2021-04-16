import requests
def geting_from_jurl_TSVer(jurl):
    values=[]
    r = requests.get(url)
    stry=r.json()
    strx=str(stry)

    print(strx)
    strxlen=len(strx)
    while (str(strx[int(strxlen)-1]) != ":"):
        strxlen-=1
    newstex=""
    for a in strx[strxlen:]:
        if a == "." or a.isnumeric() or a=="-":
            newstex=newstex+a
    print((newstex))
    if 'feeds' in stry:
        stry=stry['feeds'][0]
        if 'field1'in stry and 'field2'in stry and 'field3'in stry and 'field4'in stry and 'field5'in stry and 'field6'in stry and 'field7'in stry and 'field8'in stry:
            i=0
            for key in stry.keys():
                if i >1:
                    values.append(stry[key])
                i+=1
        else:
            values=stry['field1']
    print(values)

    return round(float(newstex))

#url = "https://api.thingspeak.com/channels/471406/feeds.json?api_key="+""+"&results=1"
#x = geting_from_jurl_TSVer(url)
#print(x)
