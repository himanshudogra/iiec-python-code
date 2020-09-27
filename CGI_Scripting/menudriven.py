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
        new_line="\n"
        new_line=new_line.replace("\n","<br />")
        print(new_line); print(new_line)
        output=output.replace("\n","<br />")
        print(output)
    else:
        print("internet is not connected, Error: ",output)

#for displaying the docker version installed on the system
elif (("check" in req) or ("show" in req) or ("update" in req) or ("run" in req) or ("tell" in req)) and (("docker version" in req) or ("container engine version" in req) or (("docker" in req) and ("version" in req))):
    docker_version=sb.getstatusoutput("sudo docker version")
    status=docker_version[0]
    output=docker_version[1]

    if status == 0:
        output=output.replace("\n","<br />")
        print(output)
    else:
        print("An Error reported while fetching the docker version",docker_version[1])

#for fetching the ipaddress of Google web servers
elif (("tell" in req) or ("show" in req) or ("update" in req) or ("check" in req) or ("verify" in req)) and (("google ipaddress" in req) or (("ip" in req) and ("google" in req)) or (("ip" in req) and ("google's" in req)) or (("ipaddress" in req) and ("google's" in req))):
    google_ip=sb.getstatusoutput("host www.google.com")
    status=google_ip[0]
    output=google_ip[1]

    if status == 0:
        print("Below are the Google's Ipaddress details:")
        new_line="\n"
        new_line=new_line.replace("\n","<br />")
        print(new_line); print(new_line)
        output=output.replace("\n","<br />")
        print(output)

    else:
        print("You don't have internet connectivity. Please check your internet connection first before using this.")

#for fetching the container details
elif (("tell" in req) or ("show" in req) or ("update" in req) or ("check" in req) or ("verify" in req)) and ((("containers" in req) and ("total" in req) and ("present" in req)) or (("containers" in req) and ("total" in req) and ("available" in req))):
    container_list=sb.getstatusoutput("sudo docker ps -aq")
    output=container_list[1]
    status=container_list[0]

    if status == 0:
        print("Here is the list of containers available:")
        new_line="\n"
        new_line=new_line.replace("\n","<br />")
        print(new_line); print(new_line)
        output=output.replace("\n","<br />")
        print(output)
    else:
        print("Error Reported:")
        new_line="\n"
        new_line=new_line.replace("\n","<br />")
        print(new_line); print(new_line)
        print(output)
