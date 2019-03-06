# Use a list comprehension to square each odd number in a list. The list is
# input by a sequence of comma-separated numbers.

items = [x for x in raw_input().split(',')]
odd = [int(x)**2 for x in items if int(x) % 2 != 0]
print odd
