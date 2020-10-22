#\s [\f\v\t\r\n]
#\S [^\f\v\t\r\n]

import re


if re.search("\w{2,20}\s\w{2,20}","Himanshu Dogra"):
    print("It is a valid name")