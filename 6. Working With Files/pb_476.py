"""
Write a Python program to reverse the content of a one file and store it in second file and also convert content of second
file into uppercase and store it in third file and also count number of Vowels in third file and also print only 2nd line from
the content of third file.

Examples:

If data file one contains the following data:
Friends are crazy, Friends are naughty !
Friends are honest, Friends are best !

Output 1:
! tseb era sdneirF ,tsenoh era sdneirF
! ythguan era sdneirF ,yzarc era sdneirF
Output 2:

! TSEB ERA SDNEIRF ,TSENOH ERA SDNEIRF
! YTHGUAN ERA SDNEIRF ,YZARC ERA SDNEIRF
Output 3:

Vowels = 22
Output 4:

! YTHGUAN ERA SDNEIRF ,YZARC ERA SDNEIRF
"""

f=open("one.txt","r")
z=f.read()
f.close()

f=open("two.txt","w+")
f.write(z[::-1])
f.seek(0)
z2=f.read()
f.close()
print(f" Output 1: \n {z2}")

f=open("three.txt" ,"w+")
f.write(z2.upper())
f.seek(0)
z3=f.readlines()
print("Output 2 : \n")
for i in z3:
    print(i,end="")


vowel=0
for i in z3:
    i=i.split(" ")
    for j in i:
        for k in j:
            if k in "AEIOU":
                vowel+=1
      
            
print(f"\noutput 3:   Vowels = {vowel}")

print("Output 4 : \n")
for i in z3:
    if i==z3[1]:
        print(i)



