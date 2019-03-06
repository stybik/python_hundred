# 1/2+2/3+3/4+...+n/n+1 

n = int(raw_input())
sum = 0.0
for i in range(1, n+1):
    sum += float(float(i)/(i+1))
print sum
