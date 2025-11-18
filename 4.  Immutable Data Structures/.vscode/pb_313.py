"""
Write a Python program to return another string similar to the input string, but with its case inverted. 
For example, input of “Mr. Ed” will result in “mR. eD” as the output string.
 Note: Use of built in swapcase function is prohibited.

 """
def reverse(s):
    n=""
    for  i in s:
        if i.islower():
            n=n+i.upper()
        elif i.isupper():
            n=n+i.lower()
        else:
            n=n+i
    return n


word=input("Enter string")
Reversed=reverse(word)
print(Reversed)