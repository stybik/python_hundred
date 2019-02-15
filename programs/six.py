import math

c = 50
h = 30
val = []
items = [x for x in raw_input().split(",")]
print items
for d in items:
   val.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print ",".join(val)