# Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

def NumGenerator(n):
   lt = range(0, n+1)
   yield filter(lambda x: (x%7 == 0 and x%5 == 0), lt)

n=int(raw_input())
values = []
for i in NumGenerator(n):
    values.append(str(i))

print ",".join(values)