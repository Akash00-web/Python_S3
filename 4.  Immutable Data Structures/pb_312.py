"""
Write a python program to check the validity of a Password.

 Primary conditions for password validation:
 1. Minimum 8 characters.
 2. The alphabet must be between [a-z]
 3. At least one alphabet should be of Upper Case [A-Z]
 4. At least 1 number or digit between [0-9]
 5. At least 1 character from [ _ or @ or $]


 Examples:
 Input: Ram@_f1234
 Output: Valid Password
 Input: Rama_fo$ab
 Output: Invalid Password
 Explanation: Number is missing

"""

def check_password(pwd):
    if len(pwd) < 8:
        return False

    lower = False
    upper = False
    digit = False
    special = False

    for ch in pwd:
        if ch.islower():
            lower = True
        elif ch.isupper():
            upper = True
        elif ch.isdigit():
            digit = True
        elif ch in "_@$":
            special = True

    return lower and upper and digit and special


password = input("Enter password: ")

if check_password(password):
    print("Password is valid.")
else:
    print("Password is NOT valid.")
