# Please write a program using generator to print the even number
# between 0 and n in comma separated form while n is input by console.


def EvenGenerator(n):
    lt = list(range(0, n+1))
    yield filter(lambda x: x % 2 == 0, lt) 

n = int(raw_input("Enter the range: "))
val = []
for i in EvenGenerator(n):
    val.append(str(i))

print ",".join(val)
