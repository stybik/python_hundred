# l = []
# for i in range(2000, 3201):
#    if(i%7 == 0) and (i%5 == 0):
#       l.append(str(i))
# print ",".join(l)


# Using lambda filter

lt = range(2000, 3201)
print list(filter(lambda x: (x % 7 == 0 and x % 5 == 0), lt))
