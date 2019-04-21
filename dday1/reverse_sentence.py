sentence = "I love you"
sentence_list = list(sentence)
sentence_list.reverse()
reversed_sentence = ''
for char in sentence_list:
    reversed_sentence = reversed_sentence + char
print(reversed_sentence)
