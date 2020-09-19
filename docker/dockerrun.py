import subprocess as sp

input=input("Enter the container Name: ")

cmd=sp.getstatusoutput("docker run -d -it --name {} ubuntu:latest".format(input))

status=cmd[0]
output=cmd[1]

#print(status)

if status == 0:
    print()
    print("Container {} launched.".format(input))
    print()
else:
    print()
    print(output)
    print()
#print(output)
