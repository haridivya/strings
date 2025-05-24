# count of vowels and consonants in the sentences
def count_vowels_consonants(s):
    vowels=0
    consonants=0
    for i in s:
        if i in'aeiouAEIOU':
            vowels+=1
        else:
            if i!=' ':
                consonants+=1
    return f'The vowels count is {vowels} and  consonants count is {consonants} in the given sentence'
s=input("Enter the word:")
print(count_vowels_consonants(s))
