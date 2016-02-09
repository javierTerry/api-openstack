import os
import sys
import novaclient.v2.client as nvclient
#import novaclient.exceptions.Unauthorized
#import novaclient.v3.client as nvclient
import json
import csv
import collections

# Read from the env vars
# TODO parse arguments in command line


class Foo(object):
    def __init__(self):
        self.name = 1
        self.uuid = 2
	self.volumens = {}
    
    def to_json(self):
        return json.dumps(self.__dict__)

def get_nova_credentials( sType):
    cred = {}
    cred['username']   = os.environ['OS_USERNAME']
    cred['api_key']    = os.environ['OS_PASSWORD']
    cred['auth_url']   = os.environ['OS_AUTH_URL']
    #cred['project_id'] = "Corte Ingles"#os.environ['OS_PROJECT_NAME']# "IMSS-1" #"UNETE_Op-07678" #"SORIANA_Op-08151"#os.environ['OS_TENANT_NAME']
    #cred['service_type'] = "volume"
    return cred


def nova_list_show(params):
	credentials = get_nova_credentials("")
	#print params
	cr = credentials.update(params)
	#print dir(credentials)
	#print type(cr)
	#print credentials
    	print "nova list"
	print credentials
	try:
	    	nc = nvclient.Client(**credentials)
		for server in nc.servers.list():
        		print "VM id= {}, name = {}".format(server.id,server.name)
	except:
    		print "Unexpected error:", sys.exc_info()[0]
    		#raise
	
def nova_list(params):
        credentials = get_nova_credentials("")
        try:
		cr = credentials.update(params)
        	nc = nvclient.Client(**credentials)
        	return nc.servers.list()
        except:
                print "Unexpected error:", sys.exc_info()[0]
                #raise

def main():
    credentials = get_nova_credentials("")
    print "main {}".format(credentials)
    nova_list(credentials)
    print "fin nova main"
    exit()
    #print credentials
    nc = nvclient.Client(**credentials)
    #exit();
    #for volume in nc.volumes.list():
	#print "Valumen" , repr(volume)
 	#volume.size

    #exit();
    #print nc.flavors.list()
    #print nc.servers.list()
    #print nc.volumes.list()
	#for volume in nc.volumes.get_server_volumes("1af9e615-68c4-48e9-bb8e-1ad8e24ece40"):
#	 print "Volume in server" , repr(volume) 
    #f = open('test.json')
    #data = json.load(f)
    #f.close()

    
    for server in nc.servers.list():
	print "VM id= {}, name = {}".format(server.id,server.name)
        attach = ""
	volumensData = []
	for volume in nc.volumes.get_server_volumes(server.id):
		volumensData.append(volume.id)
	
	#print "VM id= {}, name = {}, attach = {}".format(server.id,server.name,attach)
	data = []
	data.append("casa")
	data.append("casa2")
	json = Foo()
	json.name = server.name
	json.uuid = server.id
	json.volumens = volumensData
        print json.volumens
	print json.to_json()
#	exit()

#    for flavor in nc.flavors.list():
#	print flavor
#	repr(flavor)
	#json.dumps(flavor, sort_keys=True, indent=4)
	#print flavor.ram

def write(cadena):
    print('Creating new text file') 

    name = "test.txt" #raw_input('Enter name of text file: ')+'.txt'  # Name of text file coerced with +.txt

    try:
        file = open(name,'w')   # Trying to create a new file or open one
        file.write(cadena)
	file.close()

    except:
        print('Something went wrong! Can\'t tell what?')
        sys.exit(0) # quit Python


if __name__ == '__main__':
    	cred = {}
	cred['project_id'] = "Corte Ingles"
	nova_list(cred)

