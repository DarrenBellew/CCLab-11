import boto, requests
import boto.sqs, sys

def getKeyandId():
	res = requests.get('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
	keyId, key = res.text.split(":")
	return (keyId, key)

def messageQueue(conn, queueName):
	return conn.get_queue(queueName).count()

#Main Code
keyId, key = getKeyandId()

conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=keyId, aws_secret_access_key=key)

print ("Number of queues: " + countQueue(conn, sys.argv[1]));