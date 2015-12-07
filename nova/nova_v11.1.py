import os

import novaclient.v1_1.client as nvclient
#import novaclient.v3.client as nvclient
import json
# Read from the env vars
# TODO parse arguments in command line
def get_nova_credentials( sType):
    cred = {}
    cred['username']   = os.environ['OS_USERNAME']
    cred['api_key']    = os.environ['OS_PASSWORD']
    cred['auth_url']   = os.environ['OS_AUTH_URL']
    cred['project_id'] = "IMSS-1"#os.environ['OS_PROJECT_NAME']# "IMSS-1" #"UNETE_Op-07678" #"SORIANA_Op-08151"#os.environ['OS_TENANT_NAME']
    #cred['service_type'] = "volume"
    return cred

def main():
    credentials = get_nova_credentials("")
    print credentials
    nc = nvclient.Client(**credentials)
    #print nc.volumes.list(False)
    #volumes = nc.volumes.list()
    #print dir(volumes[0])
    #print nc.servers.list()   

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
    for server in nc.servers.list():
	#print "VM id= {}, name = {}".format(server.id,server.name)
        attach = ""
	for volume in nc.volumes.get_server_volumes(server.id):
		#print "Volume ->", repr(volume.volumeId)
		print volume.id
		attach = volume.id + "," + attach
		#print volume.human_id
		#print "Volume get->", repr(nc.voluddmes.get("31446692-49dd-4985-ab3c-add26ad83a44"))
		#print "Volume get->", repr(volume.id)
		#print "Tamano :", repr(volume.size)
	
	print "VM id= {}, name = {}, attach = {}".format(server.id,server.name,attach)
#    for flavor in nc.flavors.list():
#	print flavor
#	repr(flavor)
	#json.dumps(flavor, sort_keys=True, indent=4)
	#print flavor.ram



if __name__ == '__main__':
    main()
