import simplejson, uuid, boto, requests


def getKeyandId():
	res = requests.get('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
	keyId, key = res.text.split(":")
	return (keyId, key)

def createQueue(conn, queueName):
	conn.create_queue(queueName)
	print("queue '" + queueName + "'' is now created.")

#Main Code
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
createQueue(conn, "C13729611: " + argv[0])
