import boto, requests
import boto.sqs, sys

def getKeyandId():
	res = requests.get('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
	keyId, key = res.text.split(":")
	return (keyId, key)

def messageQueue(conn, queueName, message):
	q = conn.get_queue(queueName)

	if q != None:
		q.write(message)
		print("Message '" + m.get_body() + "' is written to queue: " + queueName )

#Main Code
keyId, key = getKeyandId()

conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=keyId, aws_secret_access_key=key)
m = Message()
m.set_body(sys.argv[2])
messageQueue(conn, "C13729611_" + sys.argv[1], m)
