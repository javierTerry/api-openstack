import sys

from nova import server 
from keystone import tenants , credenciales as cr
from utils.string import utils 

tenants = tenants.tenant_list()

credenciales =  cr.get_credentials()
#credenciales['project_id']

noVms = 0

print credenciales
print "Tenant, UUID, DESCRIPCION"
for tenant in tenants:
	print ">>>>>>>>>>>>>   CAMBIO DE TENANT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
	cr = {'project_id': utils.utf8(tenant.name)}
	#server.nova_list_show(cr)
	#exit()
	try:
		servers = server.nova_list(cr)
		for vm in servers:
			print "{},{},{},{}".format(utils.utf8(tenant.name),tenant.id,utils.utf8(tenant.description),vm.name)
			noVms += 1
	except:
		print "Unexpected error:", sys.exc_info()[0]
	#for server in servers:
	#	print "{},{},{},{}".format(utils.utf8(tenant.name),tenant.id,utils.utf8(tenant.description),server.name)	
	
print "Mumero de VM {}".format(noVms)
