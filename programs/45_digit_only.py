# Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

import re
s = raw_input("Enter a string composed of digits: ")
print re.findall("\d+",s)