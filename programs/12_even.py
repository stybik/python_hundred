# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.

val = []
for i in range(1000, 3001):
   s = str(i)
   if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
      val.append(s)
print ",".join(val)
