# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

words = raw_input("Enter a string: ").split(" ")
print " ".join(sorted(list(set(words))))