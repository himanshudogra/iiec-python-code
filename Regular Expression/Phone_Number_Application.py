import re

#\w [a-zA-Z0-9_]
#\W [^a-zA-Z0-9]

phone_no="412-324-9287"

if re.search("\w{3}-\w{3}-\w{4}",phone_no):
    print("Phone number matches.")
