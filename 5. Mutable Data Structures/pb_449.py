"""
Write Python Program to create a dictionary with the key as the first character and value as a list of words starting with
that character.

Example:

Input: Don’t wait for your feelings to change to take the action. Take the action and your feelings will change

Output:
{'D': ['Don’t'], 'w': ['wait', 'will'], 'f': ['for', 'feelings', 'feelings'], 'y': ['your', 'your'], 't': ['to', 'to', 'take', 'the', 'the'], 'c':['change', 'change'], 'a': ['action.', 'action', 'and'], 'T': ['Take']} 

"""
s = "Don’t wait for your feelings to change to take the action. Take the action and your feelings will change"

words = s.split()

output = {
    k: list(filter(lambda w, c=k: w.startswith(c), words))
    for k in set(map(lambda x: x[0], words))
}

print(output)
