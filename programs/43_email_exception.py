# Assuming that we have some email addresses in the "username@companyname.com"
#  format, please write program to print the user name of a given email
#  address.
#  Both user names and company names are composed of letters only.

import re
email_add = raw_input("Enter your email id: ")
tempo = "(\w+)@((\w+\.)(com))"
r2 = re.match(tempo, email_add)
print r2.group(1)
