import pip
try:
    from wit import Wit
except:
    #if hasattr(pip, 'main'):
    pip.main(['install', 'wit'])
    #else:
        #pip._internal.main(['install', 'wit'])
    from wit import Wit
try:
    wit_access_token="SVLQI4SRLNSTWVXJDFA5OQERBPUPHWZK"
    wit_client = Wit(wit_access_token)
except Exception as e:
    print("Wit Error :  " + str(e))

def send(query):
    wit_resp=wit_client.message(query)
    wit_resp_G={}
    wit_resp_G=wit_resp
    return(wit_resp_G)



    '''
    #wit_resp="{'_text': 'hello', 'entities': {'on_off': [{'confidence': 0.83227133750916, 'value': 'on'}], 'greetings': [{'confidence': 0.99988770484924, 'value': 'true'}], 'search_query': [{'suggested': True, 'confidence': 0.93805998563766, 'value': 'hello', 'type': 'value'}]}, 'WARNING': 'DEPRECATED', 'msg_id': '1fO0q8Z8O3C7xG61d'}"
    entity=[]

    wit_resp=str(wit_resp)
    #print(wit_resp)
    filtered_wit = {}
    if "'entities'" in wit_resp:
        count = wit_resp.index("'entities'") + len("'entities'")
        #print(count)
        while count<len(wit_resp):
            while True:
                if wit_resp[count]=="'":
                    #print("entity start point"+str(count))
                    count+=1
                    entity.append(wit_resp[count:wit_resp.index("'",count,len(wit_resp)-1)])
                    #print(entity[0])
                    break
                count+=1
            if "'confidence':" in wit_resp:
                count = wit_resp.index("'confidence':") + len("'confidence':")
                sbrk = False
                brk= False
                confidence=""
                while True:
                    if wit_resp[count].isnumeric() or wit_resp[count]==".":
                        confidence+=str(wit_resp[count])
                        sbrk = True
                        brk= False
                    else:
                        brk= True
                        if brk and sbrk:
                            entity.append(float(confidence))
                            #print(entity[1])
                            break
                    count+=1
                if "'value':" in wit_resp:
                    #print(count)
                    count = wit_resp.index("'value':") + len("'value':")
                    #print(wit_resp[count],count)
                if "'" in wit_resp[count:]:
                    start = wit_resp.index("'",count,len(wit_resp)-1)+1
                    end = wit_resp.index("'",int(wit_resp.index("'",count,len(wit_resp)-1)+1),len(wit_resp)-1)
                    value = wit_resp[start:end]
                    entity.append(value)
                    #print(entity[2])
            filtered_wit[entity[0]]=entity[1:]

            #print(wit_resp[end+])  }]
            if "}]}" in wit_resp:
                if (wit_resp.index("}]}",end+1,len(wit_resp))-wit_resp.index("}]",end+1,len(wit_resp))) ==0 and entity[0] !="datetime":
                    break
                else:
                    wit_resp=wit_resp[wit_resp.index("}]",end+1,len(wit_resp)):]
            entity=[]
            count=0
    return filtered_wit

    #print(filtered_wit)'''


#   what is the weather of tomorrow

if __name__=='__main__':
    wit_resp_G=send("hello there")

#sentence.index('g is', 10, -4)
{'_text': 'hello there', 'entities': {'on_off': [{'confidence': 0.50147241353989, 'value': 'on'}], 'greetings': [{'confidence': 0.99971348047256, 'value': 'true'}], 'reminder': [{'suggested': True, 'confidence': 0.93606001138687, 'value': 'hello there', 'type': 'value'}]}, 'WARNING': 'DEPRECATED', 'msg_id': '1WUNQ3jUYTOo6LG8W'}
