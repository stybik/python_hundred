# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.


# for row in range(rown):
#    for col in range(coloum):
#       arr[row][col] = row*col

size = raw_input("Enter the size of the array: ")
dimensions = [int(x) for x in size.split(",")]
rown = dimensions[0]
coloum = dimensions[1]
#Intialize the array with 0 using nested list comprehension
arr = [[0 for col in range(coloum)] for row in range(rown)]
arr = [[row*col for col in range(coloum)] for row in range(rown)]
print arr