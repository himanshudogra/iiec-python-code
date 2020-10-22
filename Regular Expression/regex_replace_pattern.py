import re


str="rat mat pat sat"

regex=re.compile("rat")

str=regex.sub("Rat",str)

print(str)