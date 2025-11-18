"""
Write a Python programme that accepts a string and calculate the number of uppercase letters, lowercase letters and 
number of digits.

 For example,
 Input: Hello Pyth@n is 100% easy
 Output:
 Uppercase letters : 2
 Lowercase letters : 14
 Digits : 3

"""
s = input("Enter string: ")
u = 0
l = 0
d = 0

for ch in s:
    if ch.isupper():
        u += 1
    if ch.islower():
        l += 1
    if ch.isdigit():
        d += 1

print(f"Uppercase: {u}    Lowercase: {l}    Digits: {d}")
