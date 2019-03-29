# Write a program that accepts a sequence of whitespace
# separated words as input and prints the words after
#  removing all duplicate words and sorting them
#  alphanumerically.

string = "Hello world, I am the boss boss the world should fear!"
words = string.split(" ")
print ("The answer is: ")
print (" ".join(sorted(list(set(words)))))
