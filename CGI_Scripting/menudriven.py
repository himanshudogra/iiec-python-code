#!/usr/bin/python3

print("content-type:text/html")
print()


import cgi
import subprocess as sb

form=cgi.FieldStorage()
req=form.getvalue("req")

#for checking the today's date
if (("tell" in req) or ("show" in req) or ("display" in req) or ("what's" in req)) and ((("today's" in req) and ("date" in req)) or (("today" in req) and ("date" in req))):
    date_output=sb.getstatusoutput("date +%D")
    print("Here is today's date: ",date_output[1])

#for checking the internet connectivity
elif (("tell" in req) or ("check" in req) or ("update" in req) or ("verify" in req) or ("access" in req)) and (("internet" in req) or ("net" in req) or (("net" in req) and ("working" in req)) or (("internet" in req) and ("working" in req))):
    internet_update=sb.getstatusoutput("ping -c 5 www.google.com")
    status=internet_update[0]
    output=internet_update[1]

    if status == 0:
        print("Your system is connected to internet.")
    else:
        print("internet is not connected, Error: ",output)

#for displaying the docker version installed on the system
elif (("check" in req) or ("show" in req) or ("update" in req) or ("run" in req) or ("tell" in req)) and (("docker version" in req) or ("container engine version" in req) or (("docker" in req) and ("version" in req))):
    docker_version=sb.getstatusoutput("sudo docker version")
    status=docker_version[0]
    output=docker_version[1]

    if status == 0:
        print(docker_version[1])
    else:
        print("An Error reported while fetching the docker version",docker_version[1])

#for fetching the ipaddress of Google web servers
elif (("tell" in req) or ("show" in req) or ("update" in req) or ("check" in req) or ("verify" in req)) and (("google ipaddress" in req) or (("ip" in req) and ("google" in req)) or (("ip" in req) and ("google's" in req)) or (("ipaddress" in req) and ("google's" in req))):
    google_ip=sb.getstatusoutput("host www.google.com")
    status=google_ip[0]
    output=google_ip[1]

    if status == 0:
        print("Here are the Google's Ipaddress details")
        print()
        print(output)
    else:
        print("You don't have internet connectivity. Please check your internet connection first before using this.")
