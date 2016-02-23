import sys
import os
from nova.server import Server
from nova.volumes import Volume
from nova.flavor import Flavor

from keystone import tenants , credenciales as cr
from utils.string import utils 

tenants = tenants.tenant_list()

credenciales =  cr.get_credentials()
#credenciales['project_id']

noVms = 0
server = Server()
print credenciales
print "Tenant, UUID, DESCRIPCION, NOMBRE VM,VM UUID "
for tenant in tenants:
	#print ">>>>>>>>>>>>>   CAMBIO DE TENANT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
	cr = {'project_id': utils.utf8(tenant.name)}
	try:	
		servers = server.nova_list(cr)
		for vm in servers:
			#print ">>>>>>>>>> {}, {} <<<<<<<<<<<<<".format(utils.utf8(vm.name), vm.id)
			sCsv = "{},{},{},{},{}".format(utils.utf8(tenant.name),tenant.id,utils.csvCadena(tenant.description),vm.name,vm.id)
			print sCsv
			noVms += 1
	except:
		raise
		noVms += 1

print "Numero de VM {}".format(noVms)


#if __name__ == '__main__':
#	detail_all_tenant()


