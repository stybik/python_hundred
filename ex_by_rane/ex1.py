# Reverse a sentence


sentence = raw_input("Enter a sentence: ")
first = sentence.split()
final = first[::-1]
new_sentence = ' '.join(final)
print new_sentence