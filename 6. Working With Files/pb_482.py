"""
Write a program to compare two text files. If they are different, give the line and column numbers in the files where the
first difference occurs.
Example:
File 1: python1.txt
Friends are crazy, Friends are naughty !
Friends are honest, Friends are best !
Friends are like keygen, friends are like license key !
new We are nothing without friends, Life is not possible without friends !
File 2: python2.txt
Friends are crazy, Friends are naughty !
Friends 6re honest, Friends are best !
Friends are like keygen, friends are like license key !
new We are nothing without friends, Life is not possible without friends !
Output:
line number 2 colNo. 9

"""


with open("Python1.txt","r") as f , open("Python2.txt","r") as f1:
    z1=f.readlines()
    z2=f1.readlines()
    is_mismatch=False
    min_length=min(len(z1),len(z2))

    for i in range(min_length):
        line1=z1[i]
        line2=z2[i]

        min_col=min(len(line1),len(line2))

        for j in range(min_col):
            if line1[j]!=line2[j]:
                print(f"line number {i} col No. {j+1}")
                is_mismatch=True
                break
        if is_mismatch:
            break

if not is_mismatch:
    if len(line1)!=len(line2):
        print(f" Files different at line {min_length+1} col No. 1")
    else:
        print("Both files are same")


