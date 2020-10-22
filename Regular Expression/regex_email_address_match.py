import re

email = "hdogra@redhat.com  himanshudogra96@gmail.com   himanshudogra1993@gmail.com  jack@com .@com @md.com h@mcafee.com"


print("Mathes:",len(re.findall("[\w.+-_%]{2,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", email)))

print(re.search("[\w.+-_%]{2,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", email))

print(re.findall("[\w.+-_%]{2,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", email))