import boto, requests
import boto.sqs, sys
from boto.sqs.message import Message

def getKeyandId():
	res = requests.get('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
	keyId, key = res.text.split(":")
	return (keyId, key)


	
def deleteMessage(conn, queueName):
	q = conn.get_queue(queueName)
	m = q.read(60)
	q.delete_message(m)
	return m



#Main Code
keyId, key = getKeyandId()

conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=keyId, aws_secret_access_key=key)
QUEUE = "C13729611_" + sys.argv[1]



print ("Removing message: " + deleteMessage(conn, "C13729611_" + QUEUE))
print ("Message removed from queue")