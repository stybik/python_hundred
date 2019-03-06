# Write a program that accepts a sentence and calculate
#  the number of letters and digits.

# s = raw_input()
# d={"DIGITS":0, "LETTERS":0}
# for c in s:
#     if c.isdigit():
#         d["DIGITS"]+=1
#     elif c.isalpha():
#         d["LETTERS"]+=1
#     else:
#         pass

# print "LETTERS", d["LETTERS"]
# print "DIGITS", d["DIGITS"]

s = raw_input("Enter a string: ")
numbers = sum(c.isdigit() for c in s)
words = sum(c.isalpha() for c in s)
print "Numbers : " + str(numbers) + " Words : " + str(words)
