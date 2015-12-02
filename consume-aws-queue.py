import boto, requests
import boto.sqs, sys
from boto.sqs.message import Message

def getKeyandId():
	res = requests.get('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
	keyId, key = res.text.split(":")
	return (keyId, key)

def getMessage(conn, queueName):
	m = []
	
	q = conn.get_queue(queueName)
		
		
	for i in range(0,q.count()):
		m.append(q.read(60).get_body())
	return str(m)
	
def deleteMessage(conn, queueName):
	q = conn.get_queue(queueName)
	m = q.read(60)
	q.delete_message(m)



#Main Code
keyId, key = getKeyandId()

conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=keyId, aws_secret_access_key=key)

m = getMessage(conn, "C13729611_" + sys.argv[1])
print ("Messages of queue: " + m)

print ("Removing message")
deleteMessage(conn, "C13729611_" + sys.argv[1])
m = getMessage(conn, "C13729611_" + sys.argv[1])
print ("Messages of queue " + m)
