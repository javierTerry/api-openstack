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
		#cred['auth_url']   = "http://vrrp:8774/v2.0"
		cred['project_id'] = "admin"
		#cred['tenant_name'] = "admin"
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
        	try:
                	nc = nvclient.Client(**cred)
			#print dir(nc.flavors.list())
			#exit()
                	for flavors in nc.flavors.list(is_public=None):
                        	print "Flavor id= {}, name = {},{},{},{}, is_public = {}".format(flavors.id,flavors.name, flavors.ram,flavors.vcpus, flavors.disk, flavors.is_public)
				#print dir(flavors)
        	except:
                	print "Unexpected error:", sys.exc_info()[0]
                	#raise

	
	def details(self, flavorUuid):
                try:
                        #cred = {}
                        #cred['service_type'] = "compute"
                        #cred.update(self.credGlobal)
			cred = self.credGlobal
			#print "flavor :{}<".format(flavorUuid)
                        nc = nvclient.Client(**cred)
                        #print (nc.flavors.get(id=flavorUuid))
                        #flavor = nc.flavors.find(name="GobMX-8vCPU-8GB",is_public=None)
			#print dir(flavor)
			return nc.flavors.find(id=flavorUuid, is_public=None)
                        #exit()
                except:
			#"algo"
			#print "algo"
                        print "{} -> Unexpected error: {}".format(__file__, sys.exc_info())
                        #raise
	


if __name__ == '__main__':
	flavor = Flavor()
	#flavorUuid = "1"
	flavorUuid = "03f58911-88cb-455c-b96f-6bb5b4f537a9"
	#flavorUuid="93946a83-9219-4460-89f5-03d240dab52d"
	flavorUuid="7b26cc27-8d3d-4eec-a3f5-588cac0fb1ee"
	flavorUuid = "86335b73-1e32-4391-b114-f7b9f22540c1"
	flavorUuid = "e632f3c1-a458-4e66-8490-b52fc2e4285e"
	flavor.list()
	flavorDtls = flavor.details(flavorUuid)
	print "Salida {}".format(flavorDtls)
	print dir(flavorDtls)
