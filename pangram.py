# A pangram is a sentence that contains every letter of the alphabet at least once.
#Write a function to check if a given string is a pangram.
#Example:
#"The quick brown fox jumps over the lazy dog" → True
def pangram(s):
    count=0
    for i in set(s):
        if i in 'abcdefghijklmnopqrstuvwxyz':
            count+=1
    if count==26:
        return "pangram"
    else:
        return "not pangram"
s=input("Enter the string:")
print(pangram(s))
