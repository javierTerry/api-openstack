import novaclient.v2.client as nvclient

import os, sys


class Flavor():
        credGlobal = {}


        def __init__(self):
                self.get_nova_credentials()

        def get_nova_credentials(self):
                cred = {}
                cred['username']   = os.environ['OS_USERNAME']
                cred['api_key']    = os.environ['OS_PASSWORD']
                cred['auth_url']   = "http://vrrp:35357/v2.0" 
		cred['project_id'] = "admin"
		cred['tenant_name'] = "admin"
		#cred['service_tag'] = "compute"
                self.credGlobal = cred

        def update_params_credentials(self,params):
                self.get_nova_credentials()
                #print self.credGlobal
                #print params
                self.credGlobal.update(params)
                #print self.credGlobal# =  cred
                #print cred
                #print "update {}".format(self.credGlobal)



	def list(self):
        	self.get_nova_credentials()
        	#print params
        	#cr = credentials.update(params)
		cred = self.credGlobal
        	print cred
        	try:
                	nc = nvclient.Client(**cred)
			#print dir(nc.flavors.list())
			#exit()
                	for flavors in nc.flavors.list():
                        	print "Flavor id= {}, name = {},{},{},{}".format(flavors.id,flavors.name, flavors.ram,flavors.vcpus, flavors.disk)
				#print dir(server)
        	except:
                	print "Unexpected error:", sys.exc_info()[0]
                	#raise

	
	def details(self, flavorUuid):
                try:
                        #cred = {}
                        #cred['service_type'] = "compute"
                        #cred.update(self.credGlobal)
			cred = self.credGlobal
			#print cred
                        nc = nvclient.Client(**cred)
                        #print dir(nc.flavors.find(id=flavorUuid))
                        return nc.flavors.find(id=flavorUuid)
                        #exit()
                except:
			"algo"
			#print "algo"
                        #print "{} -> Unexpected error: {}".format(__file__, sys.exc_info())
                        #raise
	


if __name__ == '__main__':
	flavor = Flavor()
	flavorUuid = "de2e8c77-efdb-4333-ae0a-818b0b5c923c"
	#flavor.list()
	flavorDtls = flavor.details(flavorUuid)
	print flavorDtls
