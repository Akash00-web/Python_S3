# Writing file  
 
f=open("abc.txt","w+")
f.write("These is a file for demo \n These is a file for demo  ")
f.write("\n These is a file for demo \n These is a file for demo  ")
f.seek(0)
z=f.read()
print(z)
f.close()

# Reverse the words and print
w=open("new.txt","w+")
w.write(z[::-1])
w.seek(0)
q=w.read()
w.close()
print(q)

# Count vowels in file and Print total count
r=open("story.txt","w+")
r.write("Python is fun and easy too learn.")
r.seek(0)
z=r.read()
r.close()

count=0
z=z.split(" ")
for i in z:
    for k in i:
        if k in "aeiouAEIOU":
            count+=1
        else:
            continue
print(f" Total vowels : {count}")

# read a multiline file and give each line number and store to new file
f=open("abc.txt","r")
z=f.read()
f.close()

w=open("numbered.txt","w+")
z=z.split("\n")
k=1
for i in z:
    w.write(f"{k}. {i} \n")
    k+=1
w.seek(0)
r=w.read()
w.close()

print(r)
    


    # Creates a new file a_names.txt and writes only the names that start with the letter 'A' into i
f=open("names.txt","w+")
f.write("""Alice
Bob 
Aoron
chrlie
Amanda""")
f.seek(0)
z=f.read()
f.close()

q=open("A_names.txt","w+")
z=z.split("\n")
for i in z:
    if i[0]=="A":
        q.write(f"{i}\n")
q.seek(0)
s=q.read()
q.close()

print(s)


# Creates a new file a_names.txt and writes only the names that start with the letter 'A' into i
# Filter Using
f=open("names.txt","r")
z=f.read()
f.close()

q=open("A_names.txt","w+")
z=z.split("\n")

names=list(filter(lambda x : x.startswith("A"),z))
for i in names:
    if i:
        q.write(f"{i}\n")

q.seek(0)
s=q.read()
q.close()

print(s)



# Replaces the word "bad" with "good" and "hate" with "love" in the program memory.
f=open("data.txt","w+")
f.write("I hate bugs. Bugs are bad")
f.seek(0)
z=f.read()
print(z)
f.close()

z=z.split(" ")
f=open("data.txt","w+")

for i in z:
    if i=="hate":
        f.write("love ")
    elif i=="bad":
        f.write("good ")
    else:    
        f.write(f"{i} ")
f.seek(0)
z=f.read()

f.close()
print(z)