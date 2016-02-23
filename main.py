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
print "Tenant, UUID, DESCRIPCION, NOMBRE VM,VM UUID, FLAVOR NAME, FLAVOR RAM (MB), FLAVOR VCPU, FLAVOR DISK (GB), VOLUME (GB), VOLUME NAME, VOLUME UUID "
for tenant in tenants:
	#print ">>>>>>>>>>>>>   CAMBIO DE TENANT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
	cr = {'project_id': utils.utf8(tenant.name)}
	#server.nova_list_show(cr)
	#exit()
	volume = Volume()
	flavors= Flavor()
	try:	
		volume.update_params_credentials(cr)
		server.update_params_credentials(cr)
		servers = server.nova_list(cr)
		for vm in servers:
			#print ">>>>>>>>>> {}, {} <<<<<<<<<<<<<".format(utils.utf8(vm.name), vm.id)
			#print (vm.flavor.values()[0])
			#print vm.flavor.values()
			#exit()
			flavorUuid = vm.flavor.values()[0]
			flavorDetails= flavors.details(flavorUuid)
			#print (flavorDetails)
			sFlavor = ",,,"
			if flavorDetails != None:
				sFlavor =  "{},{},{},{}".format(flavorDetails.name, flavorDetails.ram,flavorDetails.vcpus, flavorDetails.disk)
			sVolume = ",,"
			sVolId = ""
			for vol in volume.list_server(vm.id):
				sVolId = "{}|{}".format(vol.id, sVolId)
				print "Volume id {}".format(vm.id)
				volDetail = volume.details(vol.id)
				#sVolume = ",,"
				#if volDetail != None:
				#	sVolume = "{},{},{}".format(volDetail.name, volDetail.size, volDetail.id)
				#print sVolume
				
			sCsv = "{},{},{},{},{},{},{},{}".format(utils.utf8(tenant.name),tenant.id,utils.csvCadena(tenant.description),vm.name,vm.id,vm.status,sFlavor,sVolId)
			print sCsv
			noVms += 1
	except:
		#exit()
		#raise
		noVms += 1
		#print "{} -> Unexpected error: {}".format(__file__,sys.exc_info())
	#for server in servers:
	#	print "{},{},{},{}".format(utils.utf8(tenant.name),tenant.id,utils.utf8(tenant.description),server.name)	
	
	#noVms += 1
print "Numero de VM {}".format(noVms)


#if __name__ == '__main__':
#	detail_all_tenant()


