import sys
import os
import logging

from nova.server import Server
from nova.volumes import Volume
from nova.flavor import Flavor

from keystone import tenants
from keystone import credenciales as cr
from utils.string import utils 

def detail_all_tenant():
	#tnts = tenants.tenant_list()

	#cred =  cr.get_credentials()

	noVms = 0
	server = Server()
	#print cred
	print "VM NAME ,VM UUID, VM STATUS, FLAVOR NAME, FLAVOR RAM, RLAVOR VCPU, FALVOR DISK, VOLUME NAME, VOLUME SIZE, VOLUME ID"
	cr = {'project_id': utils.utf8("SAP SaaS Business One")}

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
			for tmpIp in vm.networks.values():
				sIpAttach = "{},{}".format(tmpIp[0],sIpAttach)
			
			sFlavor = ",,,"
			if flavorDetails != None:
				sFlavor =  "{},{},{},{}".format(flavorDetails.name, flavorDetails.ram,flavorDetails.vcpus, flavorDetails.disk)
				sVolume = ""
				volID = ""
				for temp in vm._info['os-extended-volumes:volumes_attached']:
					volID = temp.values()[0]
					#print "<<< {} <<<".format(volID)
					volDetail = volume.details(volID)
					if volDetail != None:
						sVolume = "{},{},{},{}".format(volDetail.name, volDetail.size, volDetail.id, sVolume)
								
			sCsv = "{},{},{},{},{}i,{}".format(vm.name,vm.id,vm.status,sFlavor,sVolume,sIpAttach)
			print sCsv
			noVms += 1
			
	except:
		raise
		noVms += 1

if __name__ == '__main__':
       detail_all_tenant()

