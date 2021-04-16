import wolframalpha
req=input(" QUESTION: ")
app_id=""
wolclient= wolframalpha.Client(app_id)
#res=wolclient.query(req)
res = wolclient.query(req)
#for pod in res.pods:
#    print(pod.text)
#wolasnwer = next(res.results).text
#print(wolasnwer)
print(res)
pod1 = res['pod'][1]
if (('definition' in pod1['@title'].lower()) or ('result' in  pod1['@title'].lower()) or (pod1.get('@primary','false') == 'true')):
      # extracting result from pod1
      result = resolveListOrDict(pod1['subpod'])
      print(result)
print(next(res.results).text)
