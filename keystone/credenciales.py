import os
#from keystoneclient.v3 import client
from os import environ as env
import keystoneclient.v2_0.client as ksclient
def get_credentials():
    cred = {}
    cred['username']   = os.environ['OS_USERNAME']
    cred['password']    = os.environ['OS_PASSWORD']
    cred['api_key']    = os.environ['OS_PASSWORD']
    cred['auth_url']   = "http://vrrp:35357/v2.0" 
    #cred['project_id'] = os.environ['OS_PROJECT_NAME']# "IMSS-1" #"UNETE_Op-07678" #"SORIANA_Op-08151"#os.environ['OS_TENANT_NAME']
    cred['tenant_name']= os.environ['OS_TENANT_NAME']
    #cred['service_type'] = "volume"
    return cred


if __name__ == "__main__":
	print "scriot"
	cr= get_credentials()
	print cr
	cr['auth_url'] = "http://vrrp:35357/v2.0"
	print cr
