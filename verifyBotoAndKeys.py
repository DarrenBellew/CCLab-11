import requests
res = requests.get('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
output = res.text
keyId, key = output.split(str=":")


print(keyId + " | " + key)