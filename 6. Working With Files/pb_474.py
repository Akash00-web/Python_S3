"""
Write a python program to search for a string in text files
"""
f=open("String.txt", "w+")
f.write("Nothing is impossible in these world\nIt is all about MindSet.")
f.close()

def string_search(s):
    f=open("String.txt", "r")
    z=f.readlines()
    found=1
    for i in z:
        if s in i:
            found=0
    if found==1:
        print("String not found")
    else:
        print("String founded...")

s=input("Enter string to search : ")
string_search(s)
    
