# Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print li
		
printList()
