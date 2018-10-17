#!/usr/bin/python
import json
from shade import *
simple_logging(debug=True)
conn = OperatorCloud(cloud='mordred')
usage_info = conn.get_compute_usage("openstack-dev")
info = usage_info["server_usages"]
running_instances = {}
for i in usage_info:
    if i == "server_usages":
        server_list = []
        for server in usage_info[i]:
            if server["state"] == "terminated":
                continue
            else:
                server_list.append(server)
        running_instances["server_usages"] = server_list
    else:
        running_instances[i] = usage_info[i]

print json.dumps(running_instances)
