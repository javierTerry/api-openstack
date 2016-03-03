#python tenants
#Chrstian Hernandez
#javierv31@gmail.com
#20160208 MasNEgocio - Kyo

import os
import logging
import keystoneclient.v2_0.client as ksclient
import credenciales as cr

cred = cr.get_credentials()
cred['auth_url'] = "http://vrrp:35357/v2.0"


def tenant_list_show():
	logger = logging.getLogger()
	logger.disabled = True
	keystone = ksclient.Client(**cred)
	print "TENANT , UUID, DESCIPCIONVM "
	logging.info('inicialziando keystone')
	for tenant in keystone.tenants.list():
        	#print " >>>>>>>>>>>>>> TENANT LISTADO <<<<<<<<<<<<<<<<<"
        	#print tenant.name.encode('utf-8').strip()
		#print "TENANT , UUID, DESCIPCIONVM "
		print "{}, {}, {}".format(tenant.name.encode('utf-8').strip(),tenant.id,tenant.description.encode('utf-8').strip())
		#print (tenant.to_dict())
		#	exit()
        #for user in tenant.list_users():
        #        print user.name
        #print " >>>>>>>>>>>>>> cambio de tenant <<<<<<<<<<<<<<<<<"


def tenant_list():
	keystone = ksclient.Client(**cred)
        tenants = keystone.tenants.list()
	return tenants


if __name__ == "__main__":
	logging.basicConfig(filename="keystone.log", level=logging.INFO)
        logging.info('Started')
        #mIylib.do_something()
	tenant_list_show()  
	logger = logging.getLogger()
        logger.disabled = False
        logging.info('Finished')
	
