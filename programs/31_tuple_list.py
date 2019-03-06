# Write a program to generate and print another tuple whose values are even
#  numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print tuple(filter(lambda x: x % 2 == 0, tp))
