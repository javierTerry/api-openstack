import sys
import os
import logging
import datetime

try:
	from nova.server import Server
	from nova.volumes import Volume
	from nova.flavor import Flavor

	from keystone import tenants as tnt
	from keystone import credenciales as cr
	from utils.string import utils 
except:
	print "{} -> Unexpected error: {}".format(__file__,sys.exc_info())
	print "revisa tus credenciales"

def detail_all_tenant():
	fileOut = file("myfile.dat", "w+")
	tenants = tnt.tenant_list()
	noVms = 0
	server = Server()
	header =  "Tenant, UUID, DESCRIPCION, NOMBRE VM,VM UUID, VM STATUS, FLAVOR NAME, FLAVOR RAM (MB), FLAVOR VCPU, FLAVOR DISK (GB), VOLUME NAME, VOLUME (GB), VOLUME UUID " 
	
	fileOut.write(header + "\n")
	for tenant in tenants:
			sTenant =  utils.utf8(tenant.name)
			#print ">>>>>>>>>>>>>   CAMBIO DE TENANT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
			logging.info('Started Tenant')
			cr = {'project_id': sTenant}
			volume = Volume()
			flavors= Flavor()
			logging.info("Despues de inicializar Volume and FLavor")
			try:
					volume.update_params_credentials(cr)
					server.update_params_credentials(cr)
					logging.info("Se actualiza credenciales Volume and FLavor")
					servers = server.nova_list(cr)
					logging.info("Inicia iteracion de servdiores del Tenant {}".format(sTenant))
					for vm in servers:
							try:
								flavorUuid = vm.flavor.values()[0]
								flavorDetails= flavors.details(flavorUuid)
								vmName = utils.utf8(vm.name)
								sFlavor = ",,,"
								logging.info("Detalles del Flavor uuid {}".format(flavorUuid))
								if flavorDetails != None:
									sFlavor =  "{},{},{},{}".format(flavorDetails.name, flavorDetails.ram,flavorDetails.vcpus, flavorDetails.disk)
								sVolume = ""
								sVolId = ""
								logging.info("listando Volumenes del VM {}".format(vmName))
								for temp in vm._info['os-extended-volumes:volumes_attached']:
									volID = temp.values()[0]
									volDetail = volume.details(volID)
									if volDetail != None:
											sVolume = "{},{},{},{}".format(volDetail.name, volDetail.size, volDetail.id, sVolume)
								sCsv = "{},{},{},{},{},{},{},{}".format(utils.utf8(tenant.name),tenant.id,utils.csvCadena(tenant.description),vmName,vm.id,vm.status,sFlavor,sVolume)
								#print sCsv
								fileOut.write(sCsv +"\n")
								noVms += 1
							except:
								 logging.info( "{} -> Unexpected error: {}".format(__file__,sys.exc_info()))
			except:
					#exit()
					#raise
					noVms += 1
					print "{} -> Unexpected error: {}".format(__file__,sys.exc_info())
			#for server in servers:
			#       print "{},{},{},{}".format(utils.utf8(tenant.name),tenant.id,utils.utf8(tenant.description),server.name)        

			#noVms += 1
	print "Numero de VM {}".format(noVms)


if __name__ == '__main__':
	sDate = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
	logName = sDate + "_" + os.path.splitext(__file__)[0] + ".log"
	logging.basicConfig(filename="logs/"+logName, level=logging.INFO)
	try:
		logging.info('Started')
		detail_all_tenant()
    		logging.info('Finished')
	except:
		logging.info( "{} -> Main Unexpected error: {}".format(__file__,sys.exc_info()))	


