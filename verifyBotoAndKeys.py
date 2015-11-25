import requests
res = requests.get('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')

payload = {'keyId', 'accessKey'}

headers = {}

res = requests.post(url, data=payload, headers=headers)

res.json()