"""
python program that accepts a list of numbers from the user and return the smallest  positive number that not appear in the list:

"""

n=int(input("Enter list size"))
l=[]
for i in range(1,n+1):
    n1=int(input("Enter number"))
    l.append(n1)
print(l)

s=set(l)
i=1
while i in s:
    i=i+1
print(f" smallest positive integer :{i }")