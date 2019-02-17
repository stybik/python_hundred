string = raw_input("Enter a string: ")
words = [word for word in string.split(" ")]
print " ".join(sorted(list(set(words))))