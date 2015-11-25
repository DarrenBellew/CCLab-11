import boto, requests
import boto.sqs, sys

def getKeyandId():
	res = requests.get('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
	keyId, key = res.text.split(":")
	return (keyId, key)

def deleteQueue(conn, queueName):
	conn.delete_queue(conn.create_queue(queueName))
	print("queue '" + queueName + "'' is now deleted.")

#Main Code
keyId, key = getKeyandId()
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=keyId, aws_secret_access_key=key)
createQueue(conn, "C13729611_" + sys.argv[1])
