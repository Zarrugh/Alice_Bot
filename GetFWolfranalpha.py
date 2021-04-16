import wolframalpha

def geting_from_wolframalpha(question):
    app_id = ""
    wolfclient = wolframalpha.Client(app_id)
    answer=""
    res = wolfclient.query(question)
    if res['@success'] == 'false':
        print('Question cannot be resolved')
    else:
        result = ''
        pod0 = res['pod'][0]
        pod1 = res['pod'][1]
        return(pod1['subpod']['img']['@alt']).split('.')[0]

#print(geting_from_wolframalpha("who is bill gate"))
#print(geting_from_wolframalpha("how much wood would a woodchuck chuck if woodchuck would chuck wood").split('.')[0])
