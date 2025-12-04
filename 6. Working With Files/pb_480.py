"""
File Filtering. write all lines of a file1, except those that start with a pound sign ( # ), the comment character for Python to
file2. And display data of file2.

Text file1 content:

Friends are crazy, Friends are naughty !
#Friends are honest, Friends are best !
Friends are like keygen, #friends are like license key !
We are nothing without friends, Life is not possible without friends !

Text file2 shoud be:

Friends are crazy, Friends are naughty !
Friends are like keygen,
We are nothing without friends, Life is not possible without friends !

"""
f = open("story.txt", "r")
z = f.readlines()
f.close()

f1 = open("story2.txt", "w+")

for i in z:
    if i.startswith("#"):
        continue
    if "#" in i:
        i = i.split("#")[0]+"\n"
    f1.write(i)

f1.seek(0)
z1 = f1.read()
f1.close()

print(z1)



