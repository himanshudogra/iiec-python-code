import re


str= "12345689456352729348456"


print("matches: ",len(re.findall("\d{5}",str)))

randstr="123 1234 12345 123456 1234567"


print("matches: ",len(re.findall("\d{3,5}",randstr)))