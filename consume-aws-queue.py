import boto, requests
import boto.sqs, sys

def getKeyandId():
	res = requests.get('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
	keyId, key = res.text.split(":")
	return (keyId, key)

def getMessage(conn, queueName):
	q = conn.get_queue(queueName)
	
	m = []
	for i in range(0,q.count()):
		m.append(q.read(60).get_body())
	return m

def deleteMessage(conn, queueName, message):
	q = conn.get_queue(queueName)
	q.deleteMessage(message)



#Main Code
keyId, key = getKeyandId()

conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=keyId, aws_secret_access_key=key)

m = getMessage(conn, "C13729611_" + sys.argv[1])
print ("Messages of queue: " + getMessage())

print ("Removing message " + sys.argv[2])
deleteMessage(conn, "C13729611_" + sys.argv[1], sys.argv[2])

print ("Messages of queue " + getMessage())
