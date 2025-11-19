"""
Write a Python program that takes a string input from the user and performs the following operations:

1) Print the string where each word is reversed, but the word order stays the same.

2) Create a dictionary with each word as a key and its length as the value.

3) Generate and display a list of words that contain at least 3 vowels.

4) Create a dictionary of character categories: vowels, consonants (letters of the alphabet except for the vowels), digits, and special characters including space, counting each type.

5) Display which category has the highest count.

6) Display the list of words with the highest number of unique letters (case-insensitive).

"""

st1 = "Computers 2025 are far more powerful and efficient!!"
st2 = st1.split()

rev = ""
d = {}
v = []
category = {}

vowels = 0
digits = 0
special = 0
consonants = 0
special_chars = "!@#$%&*^()_~`-+={}:<>?/.,';[]\\|\""

se = []               
unique_counts = {}     

for word in st2:
    rev += word[::-1] + " "
    d[word] = len(word)
    
    count = 0
    for ch in word:
        if ch.isdigit():
            digits += 1
        elif ch in special_chars:
            special += 1
        elif ch in "aeiouAEIOU":
            vowels += 1
            count += 1
        elif ch.isalpha():      
            consonants += 1

    if count >= 3:
        v.append(word)

    uniq_letters = {ch.lower() for ch in word if ch.isalpha()}
    unique_counts[word] = len(uniq_letters)

category["vowels"] = vowels
category["consonants"] = consonants
category["digits"] = digits
category["special"] = special + st1.count(" ")   


max_unique = max(unique_counts.values())
se = [w for w, c in unique_counts.items() if c == max_unique]

maxi = max(category.items(), key=lambda x: x[1])


print(f"""reversed words: 
{ rev} """)
print()
print(f"""word lengths: 
{d}""")
print()
print(f"""words with >=3 vowels: 
{v}""")
print()
print(f"""category counts:
{ category}""")
print()
print(f"""max category item:
{maxi[0]}""")
print()
print(f"""words with highest unique-letter count: 
{se}""")

