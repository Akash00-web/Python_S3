"""
sent the greatest number of mail messages. The program looks for 'From ' lines and
takes the second word of those lines as the person who sent the mail. The program
creates a Python dictionary that maps the sender's mail address to a count of the
number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary to
identify the sender with the maximum count (the most prolific sender)
.
Expected Output:

{'stephen.marquard@uct.ac.za': 2, 'louis@media.berkeley.edu': 3, 'zqian@umich.edu': 4, 'rjlowe@iupui.edu': 2,
'cwen@iupui.edu': 5, 'gsilver@umich.edu': 3, 'wagnermr@iupui.edu': 1, 'antranig@caret.cam.ac.uk': 1,
'gopal.ramasammycook@gmail.com': 1, 'david.horwitz@uct.ac.za': 4, 'ray@media.berkeley.edu': 1}

cwen@iupui.edu 5

"""

f=open("mbox.txt","r")
z=f.readlines()
f.close()

d={}
for i in z:
    if i.startswith("From "):
        i=i.split()
        d[i[1]]=d.get(i[1],0)+1
   
print(d)
print(f"{max(d,key=d.get)}   {max(d.values())}")
    

    