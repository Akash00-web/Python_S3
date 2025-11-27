"""
Write a function display_oddLines() to display odd number lines from the text file. Consider the following lines for the file
– friends.txt.
Friends are crazy, Friends are naughty !
Friends are honest, Friends are best !
Friends are like keygen, friends are like license key !
We are nothing without friends, Life is not possible without friends !

"""
def display_oddLines():
    f=open("friends.txt","r")
    z=f.readlines()
    for i in range(0,len(z),2):
        print(z[i])
    f.close()

display_oddLines()


