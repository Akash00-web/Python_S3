"""
Given a string S containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "{[()]}"
Output: Valid

Example 2:

Input: s = "()[]{}"
Output: Valid

Example 3:

Input: s = "[(})"
Output: Invalid

"""
s = input("Enter string with bracket only: ")

list = []
pair = {')':'(', '}':'{', ']':'['}

valid = True

for ch in s:
    if ch in "({[":
        list.append(ch)

    elif ch in ")}]":
        if not list:         # nothing to pop → invalid
            valid = False
            break
        
        top = list.pop()
        if top != pair[ch]:   # mismatch → invalid
            valid = False
            break

# After processing all characters, list must be empty
if valid and not list:
    print("Valid")
else:
    print("Invalid")




