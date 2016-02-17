import sys
import os
from nova import server, volumes
from nova.volumes import Volume

from keystone import tenants , credenciales as cr
from utils.string import utils 

#tenants = 
#tenants.tenant_list()

#credenciales =  cr.get_credentials()
#credenciales['project_id']


def detail_all_tenant():
	cred =  cr.get_credentials()
	cred['project_id'] = "Habers-Op18750"
	print cred
	cre = {'project_id': 'Habers-Op18750'}
        #server.nova_list_show(cr)
        #exit()
	noVms = 0
        volume = Volume()
	print dir(tenants)
	exit()
        try:
                volume.update_params_credentials(cre)
                servers = server.nova_list(cre)
                for vm in servers:
                        #print "{},{},{},{}".format(utils.utf8(tenant.name),tenant.id,utils.utf8(tenant.description),vm.name)
                        #print dir(vm)
                        #print vm.id
                        sVolume = ",,,"
                        #for vol in volume.list_server(vm.id):
                         #       #sVolume = "{},{},{}".format(volume.size, volume.name, volume.id)
                          #      volDetail = volume.details(vol.id)
                           #     sVolume = "{},{},{}".format(volDetail.size, volDetail.name, volDetail.id)
                                #print sVolume

                        print "{},{},{},{},{}".format(utils.utf8("habers"),"default",utils.utf8("test"),vm.name,sVolume)
                        noVms += 1
        except:
                noVms += 1
                print "{} -> Unexpected error: {}".format(__file__,sys.exc_info())
        #for server in servers:
        #       print "{},{},{},{}".format(utils.utf8(tenant.name),tenant.id,utils.utf8(tenant.description),server.name)        

	print "Numero de VM {}".format(noVms)

if __name__ == '__main__':
	detail_all_tenant()


