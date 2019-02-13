#Reverse each word of a sentence


sentence = raw_input("Enter a sentence : ")
words = sentence.split()
new_words = [word[::-1] for word in words]
new_sentence = " ".join(new_words)
print new_sentence