import sys
import os
import logging

from nova.server import Server
from nova.volumes import Volume
from nova.flavor import Flavor

from keystone import tenants as tnt
from keystone import credenciales as cr
from utils.string import utils 

def detail_all_tenant():
	tenants = tnt.tenant_list()
	noVms = 0
	#exit()
	server = Server()
	print "Tenant, UUID, DESCRIPCION, NOMBRE VM,VM UUID, VM STATUS, FLAVOR NAME, FLAVOR RAM (MB), FLAVOR VCPU, FLAVOR DISK (GB), VOLUME (GB), VOLUME NAME, VOLUME UUID "
	for tenant in tenants:
			#print ">>>>>>>>>>>>>   CAMBIO DE TENANT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
			logging.info('Started Tenant')
			#exit()
			cr = {'project_id': utils.utf8(tenant.name)}
			#server.nova_list_show(cr)
			#exit()
			volume = Volume()
			flavors= Flavor()
			logging.debug("despues de inicializar Volume and FLavor")
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
							sVolume = ""
							sVolId = ""
							for temp in vm._info['os-extended-volumes:volumes_attached']:
									volID = temp.values()[0]
									volDetail = volume.details(volID)
									if volDetail != None:
											sVolume = "{},{},{},{}".format(volDetail.name, volDetail.size, volDetail.id, sVolume)

							sCsv = "{},{},{},{},{},{},{},{}".format(utils.utf8(tenant.name),tenant.id,utils.csvCadena(tenant.description),vm.name,vm.id,vm.status,sFlavor,sVolume)
							print sCsv
							noVms += 1
			except:
					#exit()
					#raise
					noVms += 1
					#print "{} -> Unexpected error: {}".format(__file__,sys.exc_info())
			#for server in servers:
			#       print "{},{},{},{}".format(utils.utf8(tenant.name),tenant.id,utils.utf8(tenant.description),server.name)        

			#noVms += 1
	print "Numero de VM {}".format(noVms)


if __name__ == '__main__':
	logging.basicConfig(filename='myapp.log', level=logging.INFO)
    	logging.info('Started')
    	#mIylib.do_something()
	detail_all_tenant()
    	logging.info('Finished')
	#detail_all_tenant()


