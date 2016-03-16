import sys
import os
import logging
import time

from nova.server import Server
from nova.volumes import Volume
from nova.flavor import Flavor

from keystone import tenants
from keystone import credenciales as cr
from utils.string import utils 
from utils.files.base import Archivo



def detail_all_tenant(tenantName="admin"):
	"""
	
	returns : cadena separada por comas
	"""
	noVms = 0
	sCsvTmp = ""
	numMaxNets = 0
	numMaxVolumenes = 0
	server = Server()
	response = {'csv': '', 'numMaxVolumenes': 0, 'numMaxNets': 0}
	cr = {'project_id': tenantName}
	
	print (cr['project_id'])
	try:
		volume = Volume()
		flavors= Flavor()
		volume.update_params_credentials(cr)
		server.update_params_credentials(cr)
		servers = server.nova_list(cr)
		for vm in servers:
			flavorUuid = vm.flavor.values()[0]
			flavorDetails= flavors.details(flavorUuid)
			sIpAttach = ""
			numNets = 0
			for tmpIp in vm.networks.values():
				numNets += 1
				sIpAttach = sIpAttach + "-" + tmpIp[0]
				if numNets > numMaxNets:
					numMaxNets = numNets
							

			sFlavor = ",,,"
			if flavorDetails != None:
				sFlavor =  "{},{},{},{}".format(flavorDetails.name, flavorDetails.ram,flavorDetails.vcpus, flavorDetails.disk)
				sVolume = ""
				volID = ""
			
			numVolumenes = 0
			sVolume = ",,,"
			for temp in vm._info['os-extended-volumes:volumes_attached']:
				volID = temp.values()[0]
				volDetail = volume.details(volID)
				if volDetail != None:
					sVolume = "{},{},{},{}".format(volDetail.name, volDetail.size, volDetail.id, sVolume)
					numVolumenes += 1
					if numVolumenes > numMaxVolumenes:
						numMaxVolumenes = numVolumenes

								
			sCsvTmp = sCsvTmp + "{},{},{},{},{},{}\n".format(vm.name,vm.id,vm.status,sFlavor,sIpAttach,sVolume)
			noVms += 1
			
	except:
		raise
		noVms += 1
	response['numMaxVolumenes'] = numMaxVolumenes
	response['numMaxNets'] = numMaxNets
	response['csv'] = sCsvTmp	
	return response


if __name__ == '__main__':
	start_time = time.time()
	print sys.argv[1]
	sTenantName = ""
	try:	
		sTenantName = sys.argv[1]
		if not (sys.argv[1]):
			raise Exception("cadena en blanco")

		
	except:
		#raise
		sTenantName = raw_input("ingrese el nombre del tenant ")
	
	print ">>>>"  + sTenantName
	handle = Archivo(sTenantName + ".csv")
	tenantName = "SAP SaaS Business One"
       	response = detail_all_tenant(sTenantName)
	cabecera = "VM NAME ,VM UUID, VM STATUS, FLAVOR NAME, FLAVOR RAM, FLAVOR VCPU, FLAVOR DISK,IP Attached,"#, VOLUME NAME, VOLUME SIZE, VOLUME ID\n"
	#for x in range(1, response['numMaxNets'] + 1 ):
	#	cabecera = cabecera + "IP ATTACHED ({}),".format(x)

	for x in range(1, response['numMaxVolumenes'] + 1):
		cabecera = cabecera + "VOLUME NAME ({}) , VOLUME SIZE ({}), VOLUME UUID ({}),".format(x,x,x)

	handle.write(cabecera + "\n")
	handle.write(response['csv'])
	#handle.close()

	print("--- %s seconds ---" % (time.time() - start_time))

