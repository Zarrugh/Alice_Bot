import wolframalpha
app_id = 'P9HHPY-GQYKA25LPR'  # get your own at https://products.wolframalpha.com/api/
client = wolframalpha.Client(app_id)

res = client.query('temperature in Washington')

#for pod in res.pods:
    #print(pod)



print(next(res.results).plainText)
