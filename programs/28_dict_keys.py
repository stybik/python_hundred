# Define a function which can generate a dictionary where the keys are numbers
#  between 1 and 20 (both included) and the values are square of keys. 
# The function should just print the keys only.

numbers = int(raw_input("Enter a number: "))
dic = {n: n**2 for n in range(1, numbers)}
print dic.keys()
