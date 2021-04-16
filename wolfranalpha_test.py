# import wolframalpha
#
# req=input(" QUESTION: ")
# app_id=""
# wolclient= wolframalpha.Client(app_id)
#
# #res=wolclient.query(req)
# res = wolclient.query(req)
# #for pod in res.pods:
# #    print(pod.text)
# #wolasnwer = next(res.results).text
# #print(wolasnwer)
# print(next(res.results).text)
#*******************************************************************************
import wolframalpha
question = input('Question: ')
app_id = ""
wolfclient = wolframalpha.Client(app_id)
answer=""
res = wolfclient.query(question)

#for result in res.results:
#    answer+= result.text
try:
    answer= next(res.results).text
except StopIteration:
    count=0
    for pod in res.pods:
        if ('{p.text}'.format(p=pod) != None) and ('{p.text}'.format(p=pod) != "None") and count>3:
            answer+= '{p.text}'.format(p=pod)+", "
            count+=1
print(answer)
