# 🔸Compress a String
def compress_string(word):
    s=''
    for i in word:
        if i not in s:
         s+=i+str(word.count(i))
    return s
s=input("Enter the string:")
print(compress_string(s))
        
