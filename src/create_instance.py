#!/usr/bin/python
from shade import *

# Initialize and Turn on debugging
simple_logging(debug=True)

# Intialize the cloud connection
conn = openstack_cloud(cloud='mordred')

print "creating the instance"

'''
keypair_name = "shadetest"
pub_key_file = "/home/sailakshmi/.ssh/shadetest.pem.pub"

if conn.search_keypairs(keypair_name):
    print('Keypair already exists. Skipping import.')
else:
    conn.create_keypair(keypair_name, open(pub_key_file, 'r').read().strip())
'''

conn.create_server("Centos-test2",image="Centos7",flavor="m1.tiny",wait=True, auto_ip=False,key_name="test") 

