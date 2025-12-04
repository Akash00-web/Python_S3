"""
Write a python program to read a text file “Story.txt” and print only word starting with ‘I’ in reverse order.

Example: If value in text file is : ‘INDIA IS MY COUNTRY’

Output will be: ‘AIDNI SI MY COUNTRY’

"""
f=open("story.txt" ,"w+")
f.write("INDIA IS MY COUNTRY")
f.seek(0)
z=f.read()
f.close()

z1=z.split()
z2=""
for i in z1:
    if i[0]=="I":
        i=i[::-1]
        z2=z2+i+" "
    else:
        z2=z2+i+" "

print(z2)