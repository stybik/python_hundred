# Write a program which accepts a sequence of comma
#  separated 4 digit binary numbers as its input and then
#  check whether they are divisible by 5 or not. The
#  numbers that are divisible by 5 are to be printed in a
#  comma separated sequence.

# intp = int(p, 2) => To convert binary number into
#  Decimal, we have to use the python built-in int
#  function, which takes the binary number and the base
#  of number system as an argument.

# items = [x for x in raw_input().split(',')]
# val = []
# for p in items:
#    intp = int(p, 2)
#    if intp % 5 == 0:
#       val.append(p)

# print ','.join(val)


items = [x for x in raw_input().split(',')]
decimal = list(map(lambda x: int(x, 2), items))
print list(filter(lambda x: x % 5 == 0, decimal))
