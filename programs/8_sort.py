# Write a program that accepts a comma
# separated sequence of words as input and
# prints the words in a comma-separated sequence
# after sorting them alphabetically.

val = [x for x in raw_input().split(",")]
val.sort()
print ",".join(val)
