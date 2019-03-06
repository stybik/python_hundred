# n = int(raw_input("Enter a number: "))

# d = dict()
# for i in range(1, n+1):
#    d[i] = i*i
# print d

# Using dictionary comprehension

numbers = int(raw_input("Enter a number: "))
print {n: n**2 for n in range(1, numbers)}