size = raw_input()
dimensions = [int(x) for x in size.split(",")]

rown = dimensions[0]
coloum = dimensions[1]
#Intialize the array with 0
arr = [[0 for col in range(coloum)] for row in range(rown)]

for row in range(rown):
   for col in range(coloum):
      arr[row][col] = row*col

print arr