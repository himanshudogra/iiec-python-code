#!/usr/bin/python3

print("content-type: text/html")
print()

print("<TITLE>CGI</TITLE>")
print("<H2>Student details</H2>")

import cgi
form=cgi.FieldStorage()


print("<p>Name:",form["name"].value)
print("<p>Phone:",form["phone"].value)
print("<p>")
'''
if form.getvalue('g'):
    gender=form.getvalue('g')
else:
    gender='Not Set'
'''
#print("<p>Gender:%s" % gender)
print("<p>Gender:",form.getvalue("g"))
print("<p>Choice of Lang:",form.getlist("c"))
