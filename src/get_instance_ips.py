#!/usr/bin/python
import json
from shade import *
simple_logging(debug=True)
conn=openstack_cloud(cloud='mordred')


info =conn.get_server('cmda-final-demo')
print(info["public_v4"])
print(info["private_v4"])
