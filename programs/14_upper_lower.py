# Write a program that accepts a sentence and calculate the number of upper
# case letters and lower case

# s = raw_input()
# d={"UPPER CASE":0, "LOWER CASE":0}
# for c in s:
#     if c.isupper():
#         d["UPPER CASE"]+=1
#     elif c.islower():
#         d["LOWER CASE"]+=1
#     else:
#         pass
# print "UPPER CASE", d["UPPER CASE"]
# print "LOWER CASE", d["LOWER CASE"]

s = raw_input("Enter a string: ")
upper = sum(c.isupper() for c in s)
lower = sum(c.islower() for c in s)
print "Uppercase : " + str(upper) + " Lowercase : " + str(lower)
