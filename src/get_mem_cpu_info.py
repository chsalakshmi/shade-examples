#!/usr/bin/python
import shade
from shade import *

simple_logging(debug=True)
#conn=shade.OpenStackCloud(cloud='mordred')
conn = shade.OperatorCloud(cloud='mordred')

# To get the information about available flavours
flavors = conn.list_flavors()
for i in flavors:
    print "printing each flavour information"
    print "printing the mem information %s" %(i['ram'])
    print "printing the cpu information %s" %(i['vcpus'])
    print i


info = conn.get_aggregate("openstack-dev")
print info

op_conn = OperatorCloud(auth_url='http://10.1.4.205:5000/')
machine_info = op_conn.get_machine("test1")
print machine_info 

#info = op_conn.get_aggregate("openstack-dev")
#print info
