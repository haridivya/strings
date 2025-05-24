#check wheather given word is palindrome or not
# Method 1

def palindrome(text):
    if text[::-1]==text:
        return "It is a Palindrome"
    else:
        return 'Not a Palindrome'
text=input("Enter the Word:")
print(palindrome(text))

#Method 2

def palindrome(text):
    word=''.join(reversed(text))
    return 'palindrome' if word==text else 'not palindrome'
text=input("Enter the Word:")
print(palindrome(text))
