#Make last word of each word in sentence capital

sentence = raw_input("Enter a sentence : ")
new_sentence = (" ".join(word[::-1] for word in sentence.split(" "))).title()
new_sentence = " ".join(word[::-1] for word in new_sentence.split(" "))
print new_sentence