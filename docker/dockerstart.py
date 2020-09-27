#!/usr/bin/python3

# Server is handling the requests with the HTML header.
print("content-type:text/html")
print()

import subprocess as sp
import cgi

form=cgi.FieldStorage()

container_name=form.getvalue("container_name")
action=form.getvalue("container_start")

cmd=sp.getstatusoutput("sudo docker start {}".format(container_name))


status=cmd[0]
output=cmd[1]

if status == 0:
    print()
    print("container {} has started successfully".format(container_name))
    print()
else:
    print()
    print(output)
    print()
