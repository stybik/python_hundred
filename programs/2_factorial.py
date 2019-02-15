#Recursion

def fact(x):
   if(x == 0):
      return 1
   return x * fact(x-1)

x = int(raw_input())
print fact(x)

#Without Recursion

# n=int(input("Enter number:"))
# fact = 1
# while(n > 0):
#     fact = fact*n
#     n = n-1
# print(fact)