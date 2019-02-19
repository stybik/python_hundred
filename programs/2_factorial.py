#Recursion

# def fact(x):
#    if(x == 0):
#       return 1
#    return x * fact(x-1)

# x = int(raw_input())
# print fact(x)



#Using Lambda reduce
n = int(raw_input())
print reduce(lambda x,y: x*y, range(1,n+1))