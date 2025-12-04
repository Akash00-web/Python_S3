"""
Write a python program to extract a list of all four-letter words that start and end with the same letter from a given text
file. 

"""
f=open("mbox.txt","r")
z=f.read()
f.close()

z1=z.split()
list=[]
for i in z1:
    if len(i)==4:
        if i[0]==i[-1]:
            list.append(i)
print(list)