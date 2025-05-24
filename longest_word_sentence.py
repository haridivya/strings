# to find out the longest word in the given sentence
def longest_word_sentence(sentence):
    words=sentence.split(' ')
    max_word=''
    for i in words:
        if len(i)>len(max_word):
            max_word=i
    return max_word
sentence=input("Enter the sentence")
print(longest_word_sentence(sentence))
