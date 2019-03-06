# Write a program that accepts sequence of lines as
# input and prints the lines after making all characters
#  in the sentence capitalized.

lines = []
while True:
    s = raw_input()
    if s:
        lines.append(s.upper())
    else:
        break

for sentence in lines:
    print sentence
    