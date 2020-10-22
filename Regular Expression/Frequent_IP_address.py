import re

with open('/Users/hdogra/test') as fh:
    fstring=fh.readlines()

pattern=re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

ip_list=[]

for i in fstring:
    ip_list.append(pattern.search(i)[0])
    
ip_list.sort()

print(ip_list,"\n")

from collections import Counter

def most_frequent(ip_list):
    most=[word for word, word_count in Counter(ip_list).most_common(5)]
    print (most)

most_frequent(ip_list)