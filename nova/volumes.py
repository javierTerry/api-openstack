#from novaclient.client import Client
#from novaclient.v1_1 import client
from novaclient.v2 import client
import novaclient.v2.client as nvclient

import os, sys


class Volume():
	credGlobal = {}
	

	def __init__(self):
		self.get_nova_credentials()
	
	def get_nova_credentials(self):
    		cred = {}
    		cred['username']   = os.environ['OS_USERNAME']
    		cred['api_key']    = os.environ['OS_PASSWORD']
    		cred['auth_url']   = os.environ['OS_AUTH_URL']
    		#cred['service_type'] = "volume"
    		self.credGlobal = cred

	def update_params_credentials(self,params):
		self.get_nova_credentials()
		#print self.credGlobal
		#print params
		self.credGlobal.update(params)
		#print self.credGlobal# =  cred
		#print cred
		#print "update {}".format(self.credGlobal)
	
	
	def nova_list_show(self):
		"""
        	lista los volumens atachados en todo el tenent  en base a las credenciales
		
		require service_type volume
		Returns on success; raises :exc:`exceptions.Unauthorized` if the
        	credentials are wrong.
        	"""
	
        	#credentials = get_nova_credentials()
        	#print params
        	#cr = credentials.update(params)
        	#print dir(credentials)
        	#print type(cr)
        	#print credentials
        	print "nova list"
        	print self.credGlobal
	       	try:
                	nc = nvclient.Client(**self.credGlobal)
			#print dir(nc.volumes.list())
			#exit()
                	for volume in nc.volumes.list():
                        	print "Volume id= {}, name = {}, size {} GB, {}".format(volume.id,volume.name, volume.size,volume.user_id)
				#print dir(server)
        	except:
                	print "Unexpected error:", sys.exc_info()[0]
                	#raise


	def list():
        	credentials = get_nova_credentials()
        	cr = credentials.update(params)
        	try:
                	nc = nvclient.Client(**credentials)
                	return nc.volumes.list()
        	except:
                	print "Unexpected error:", sys.exc_info()[0]
                	#raise

	def list_server_show(self, serverUuid):
        	#credentials = get_nova_credentials()
        	#cr = credentials#.update(params)
		#print "credencials volume"
		print self.credGlobal
        	try:
                	nc = nvclient.Client(**self.credGlobal)
			#print dir(nc.volumes.get('d1adaa79-776f-456b-8543-833744d0d282'))
			#exit()
			#for volume in nc.volumes.get_server_volumes(ui):
			#	print (volume.to_dict())
			#exit()
			#return nc.volumes.get_server_volumes(serverUuid)
			#for server in nc.servers.list():
        		#	print "VM id= {}, name = {}".format(server.id,server.name)
        		#	attach = ""
        		#	volumensData = []
        		for volume in nc.volumes.get_server_volumes(serverUuid):
                		#volumensData.append(volume.id)
				print volume.id
				#print (nc.volumes.get_server_volumes('e6149112-9ec6-426d-be36-83a880c1430e'))
		
			#print "fin TEst"
			#exit()
                	#return nc.volumes.list()
        	except:
                	print "{} -> Unexpected error: {}".format(__file__, sys.exc_info()[0])
                	#raise

	def list_server(self, serverUuid):
        	try:
			nc = nvclient.Client(**self.credGlobal)
			return nc.volumes.get_server_volumes(serverUuid)
		except:
			print "{} -> Unexpected error: {}".format(__file__, sys.exc_info()[0])
			#raise


	def details(self,volumeId):
		try:
			cred = {}
			cred['service_type'] = "volume"
			cred.update(self.credGlobal)
			nc = nvclient.Client(**cred)
                	#print dir(nc.volumes.get(volumeId))
			return nc.volumes.get(volumeId)
                	#exit()
		except:
                        print "{} -> Unexpected error: {}".format(__file__, sys.exc_info()[0])
                        #raise


		

if __name__ == '__main__':
        cred = {}
        cred['project_id'] = "Corte Ingles"
	#cred['service_type'] = "volume"
        volume = Volume()
	volume.update_params_credentials(cred)
	#volume.nova_list_show()
	#volume.nova_list_show()
	#get(cred)
	#Volume().update_params_credentials(cred)
	ui = "e6149112-9ec6-426d-be36-83a880c1430e"
	#volume.list_server_show(ui)
	volume.list_server(ui)
	volumeId = "d1adaa79-776f-456b-8543-833744d0d282"
	volume.details(volumeId)

