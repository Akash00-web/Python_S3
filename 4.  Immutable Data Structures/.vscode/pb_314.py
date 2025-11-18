"""
Write a Python program to create a Caesar encryption.
 Note: In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar 
shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in 
which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For 
example, with a right shift of 3, A would be replaced by D, E would become H, and so on. The method is named 
after Julius Caesar, who used it in his private correspondence.
 For Example:
 Input Text  : LJIET ENG
 Shift : 3
 Cipher:  OMLHW HQJ
"""
def shift(s, n):
    d = ""
    for i in s:
        if i.isnumeric() or i.isspace():
            d += i
        else:
            a = chr(ord(i) + n)
            d += a
    return d

w = input('Enter string: ')
n1 = int(input("Enter number: "))
r = shift(w, n1)
print(r)

