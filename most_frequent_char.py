Write a function to find the most frequent character in a string (ignore spaces).
Example:
"banana" → 'a' appears 3 times
def most_frequent_char(s):
    frequent_char=''
    count=0
    for i in s:
        if s.count(i)>count:
            frequent_char=i
            count=s.count(i)
    return frequent_char
s=input("Enter a string:")
print(most_frequent_char(s))
