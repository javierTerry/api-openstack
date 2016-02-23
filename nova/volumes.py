#from novaclient.client import Client
#from novaclient.v1_1 import client
from novaclient.v2 import client
import novaclient.v2.client as nvclient

import os, sys


class Volume():
	credGlobal = {}
	credService = {}
	nova = ""
	novaService = ""

	def __init__(self):
		self.get_nova_credentials()
		self.nova = nvclient.Client(**self.credGlobal)
		self.novaService = nvclient.Client(**self.credService)
	
	def get_nova_credentials(self):
    		cred = {}
    		cred['username']   = os.environ['OS_USERNAME']
    		cred['api_key']    = os.environ['OS_PASSWORD']
    		cred['auth_url']   = "http://vrrp:35357/v2.0"#os.environ['OS_AUTH_URL']
    		#cred['service_type'] = "volume"
		cred['project_id'] = "admin"
    		self.credGlobal = cred
		cred['service_type'] = "volume"
		self.credService = cred
		

	def update_params_credentials(self,params):
		self.get_nova_credentials()
		#print self.credGlobal
		#print params
		self.credGlobal.update(params)
		self.nova = nvclient.Client(**self.credGlobal)
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
        		for volume in self.nova.volumes.get_server_volumes(serverUuid):
				print volume.id
				details =  self.details(volume.id)
				print "name = {}, size = {} GB, volume uuid = {}".format(details.name, details.size, details.id)
		
			#print "fin TEst"
			#exit()
                	#return nc.volumes.list()
        	except:
                	print "{} -> Unexpected error: {}".format(__file__, sys.exc_info()[0])
                	#raise

	def list_server(self, serverUuid):
        	try:
			return self.nova.volumes.get_server_volumes(serverUuid)
		except:
			#print "{} -> Unexpected error: {}".format(__file__, sys.exc_info()[0])
			#raise
			"debug"


	def details(self,volumeId):
		try:
			#cred = {}
			#cred['service_type'] = "volume"
			#self.update_params_credentials(cred)
			return self.nova.volumes.get(volumeId)
		except:
                        print "{} -> Unexpected error: {}".format(__file__, sys.exc_info()[0])
                        #raise


		

if __name__ == '__main__':
        cred = {}
        #cred['project_id'] = "Corte Ingles"
	#cred['service_type'] = "volume"
        volume = Volume()
	volume.update_params_credentials(cred)
	#volume.nova_list_show()
	#volume.nova_list_show()
	#get(cred)
	#Volume().update_params_credentials(cred)
	ui = "12d95c5e-759c-42da-8887-112dc54d65ce"
	#ui = "add9bc78-88d6-4f9d-85ff-2f4532a4c120"
	#ui = "ca67690f-e5f8-4bcf-9c39-16367962a67b"
	#volume.list_server_show(ui)
	volume.list_server_show(ui)
	
	#volumeId = "d1adaa79-776f-456b-8543-833744d0d282"
	#volume.details(volumeId)

