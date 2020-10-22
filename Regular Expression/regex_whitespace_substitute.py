import re


str='''The skyhigh is one of the best
CASB company which has
shadow and sanction IT products.
'''

print(str)
regex=re.compile("\n")


new_str=regex.sub(" ",str)

print(new_str)

#\b: backspace
#\t: tab
#\r: carriage return
#\f: form feed
#\v: vertical tab