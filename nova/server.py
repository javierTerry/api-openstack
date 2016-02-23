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

class Server():

	credGlobal = {}
	nova = ""

	def __init__(self):
                self.get_nova_credentials()
		self.nova =  nvclient.Client(**self.credGlobal)

        def get_nova_credentials(self):
                cred = {}
                cred['username']   = os.environ['OS_USERNAME']
                cred['api_key']    = os.environ['OS_PASSWORD']
                cred['auth_url']   = "http://vrrp:35357/v2.0"
                cred['project_id'] = "admin"
                #cred['tenant_name'] = "admin"
                #cred['service_tag'] = "compute"
                self.credGlobal = cred

        def update_params_credentials(self,params):
                self.get_nova_credentials()
                #print self.credGlobal
                #print params
                self.credGlobal.update(params)
		self.nova = nvclient.Client(**self.credGlobal)
                #print self.credGlobal# =  cred
                #print cred
                #print "update {}".format(self.credGlobal)

	def show(self,uuid):
		try:
			#print "uuid : {}".format(uuid)
			#print (self.nova.servers.get(uuid))
			return self.nova.servers.get(uuid)
			#print (self.nova.servers.find(uuid))
		except:
			raise
			""
					
		
	def nova_list_show(self,params):
			#credentials = self.get_nova_credentials()
			#print params
			#cr = credentials.update(params)
			#print dir(credentials)
			#print type(icr)
			#print credentials
			print "nova list"
			print self.credGlobal
			try:
					#nc = nvclient.Client(**self.credGlobal)
					for server in self.nova.servers.list():
						print dir(server)
						print "VM id= {}, name = {}, status= {}".format(server.id,server.name, server.status)
			except:
					print "Unexpected error:", sys.exc_info()[0]
					raise

	def nova_list(self,params):
			#credentials = self.get_nova_credentials()
			try:
					#cr = credentials.update(params)
					#nc = nvclient.Client(**credentials)
					
					return self.nova.servers.list()
			except:
					print "Unexpected error:", sys.exc_info()[0]
					#raise

	def main(self):
		credentials = get_nova_credentials("")
		print "main {}".format(credentials)
		nova_list(credentials)
		print "fin nova main"
		exit()


if __name__ == '__main__':
	server = Server()
	#server.nova_list()
        cred = {}
        cred['project_id'] = "Copiloto Satelital"
	server.update_params_credentials(cred)
        server.nova_list_show(cred)
	#print servers
	#server.nova_list_show(cred)
	#uuid  = "17757484-09a9-4d74-b0e6-dc03b70dfed0"
	#flavorUuid = "86335b73-1e32-4391-b114-f7b9f22540c1"
	#vm = server.show(uuid)
	#print (vm.flavor)
	#print (vm.flavor.values())
	#print (vm.flavor.values()[0])
	#print vm.flavor.find(id=flavorUuid)
	#print "VM id= {}, name = {}".format(vm.id,vm.name)

