import subprocess as sp
import cgi

#storing the HTML form's field info into form variable.
form=cgi.FieldStorage()

os_name=form.getvalue("x")
os_image=form.getvalue("i")

cmd=sp.getstatusoutput("sudo docker run -d -it --name {} {}".format(os_name,os_image))

status=cmd[0]
output=cmd[1]

#print(status)

if status == 0:
    print()
    print("Container {} launched.".format(os_name))
    print()
else:
    print()
    print(output)
    print()
#print(output)
