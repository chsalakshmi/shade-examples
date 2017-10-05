#!/usr/bin/python
from shade import *
simple_logging(debug=True)
conn=openstack_cloud(cloud='mordred')
images = conn.list_images()
for image in images:
    print "image information" 
    print image
    

print "======================"
keypairs=conn.list_keypairs()
print "+++++++++++++++++ listing keypairs info"
print keypairs

# To get the information about available flavours
flavors = conn.list_flavors()
for i in flavors:
    print i


# Get the information of flavor by ram size
flavor = conn.get_flavor_by_ram(512)
print "*********** get the information of flavor by ram size"
print flavor


# get the image information for the given image
image_name = 'UbuntuServer14.04'
image = conn.get_image(image_name)
print "printing the image information"
print image

# get the list of instances
instances = conn.list_servers()
for instance in instances:
    print "printing the instance infomation"
    print instance






