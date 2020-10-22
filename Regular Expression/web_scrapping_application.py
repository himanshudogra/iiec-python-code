import urllib.request

import re


url="http://www.summet.com/dmsi/html/codesamples/addresses.html"

response=urllib.request.urlopen(url)

html = response.read()

htmlstr=html.decode()


pdata=re.findall("\(\d{3}\)\s\d{3}-\d{4}",htmlstr)

for i in pdata:
    print(i)