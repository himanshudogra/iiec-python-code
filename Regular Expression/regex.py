import re

Nameage= '''
Himanshu is 28 and Sana is 30.
Sahil is 29 and Monika is 28.
'''
#re.findall provide the list of all the matches. 

Age=re.findall(r'\d{1,3}',Nameage)
Name=re.findall(r'[A-Z][a-z]*',Nameage)

ageDict={}
x=0


for eachname in Name:
    ageDict[eachname]=(Age[x])
    x+=1

print(ageDict)
