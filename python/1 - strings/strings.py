sentence = 'This is a TEST sentence. '


sentence[5]


sentence[5:10]


len(sentence)


strip_sentence = sentence.strip()


lower_sentence = sentence.lower()


upper_sentence = sentence.upper()


cool_sentence = sentence.replace('TEST', 'cool')


double_sentence = sentence + sentence


spaced_double_sentence = sentence, sentence


index_test_in_sentence = sentence.index('TEST')


find_test_in_sentence = sentence.find('TEST')


find_test_in_sentence = sentence.find('TEST', 5, 10)


sentence_split = sentence.strip().lower().split(' ')
word_count = 0

for word in sentence_split:
    new_word = word[0].upper() + word[1:]
    sentence_split[word_count] = new_word
    word_count += 1

upper_each_word_sentence = ' '.join(sentence_split)


joe_age = 25
formatted_sentence = "My first name is {first_name}, I'm {age} years old.".format(first_name = "Joe", age = joe_age)