'''
 Capitalize First Letter of Each Word
Problem:
Write a function that takes a string and returns it with the first letter of each word capitalized.

Example:
"hello world" → "Hello World"
'''
def capitalize_words(s):
    word=s.split(' ')
    temp=[]
    for i in word:
        temp.append(i.capitalize())
    return ' '.join(temp)
s=input("Enter the string:")
print(capitalize_words(s))
