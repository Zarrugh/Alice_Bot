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
    wit_access_token=""
    wit_client = Wit(wit_access_token)
except Exception as e:
    print("Wit Error :  " + str(e))
while True:

    print("please enter a sentence to send it to WIT server: \n \n")
    wit_resp=wit_client.message(str(input()))
    print(wit_resp)
    print()
    print()
    #wit_resp="{'_text': 'hello', 'entities': {'on_off': [{'confidence': 0.83227133750916, 'value': 'on'}], 'greetings': [{'confidence': 0.99988770484924, 'value': 'true'}], 'search_query': [{'suggested': True, 'confidence': 0.93805998563766, 'value': 'hello', 'type': 'value'}]}, 'WARNING': 'DEPRECATED', 'msg_id': '1fO0q8Z8O3C7xG61d'}"
    entity=[]
'''
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

    print(filtered_wit)
'''

#   what is the weather of tomorrow



#sentence.index('g is', 10, -4)
