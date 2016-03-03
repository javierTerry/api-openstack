import sys
import os
import logging

from nova.server import Server
from nova.volumes import Volume
from nova.flavor import Flavor

from keystone import tenants , credenciales as cr
from utils.string import utils 

tenants = tenants.tenant_list()

credenciales =  cr.get_credentials()

noVms = 0
server = Server()
print credenciales
print "VM NAME ,VM UUID, VM STATUS, FLAVOR NAME, FLAVOR RAM, RLAVOR VCPU, FALVOR DISK, VOLUME NAME, VOLUME SIZE, VOLUME ID"
#for tenant in tenants:
	#print ">>>>>>>>>>>>>   CAMBIO DE TENANT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
cr = {'project_id': utils.utf8("Copiloto Satelital")}#Corte Ingles")}

try:
	volume = Volume()
        flavors= Flavor()
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
			sVolume = ""
			volID = ""
			#print (len(vm._info['os-extended-volumes:volumes_attached']))
		for temp in vm._info['os-extended-volumes:volumes_attached']:
			volID = temp.values()[0]
			print "<<< {} <<<".format(volID)
			volDetail = volume.details(volID)
			#sVolId = "{}|{}".format(volID, sVolId)
			#print "Volume id {}".format(volID)
			#volDetail = volume.details(vol.id)
			#sVolume = ""
			if volDetail != None:
				sVolume = "{},{},{},{}".format(volDetail.name, volDetail.size, volDetail.id, sVolume)
				#print sVolume

		sCsv = "{},{},{},{},{}".format(vm.name,vm.id,vm.status,sFlavor,sVolume)
		print sCsv
		noVms += 1
except:
	raise
	noVms += 1

#name__ == '__main__':
#       detail_all_tenant()

