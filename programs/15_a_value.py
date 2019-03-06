# Write a program that computes the value of a+aa+aaa+aaaa with a given
# digit as the value of a.

# a = raw_input()
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# n4 = int( "%s%s%s%s" % (a,a,a,a) )
# print n1+n2+n3+n4

a = raw_input("Enter the value of a : ")
length = 4
print sum(int(str(a) * i) for i in range(1, length+1))
