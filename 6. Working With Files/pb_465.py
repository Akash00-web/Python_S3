"""
Write a function cust_data() to ask user to enter their names and age to store data in customer.txt file.
"""
f=open("customer.txt","w+")

def cust_data():
    n=int(input("Enter total customers numbers"))
    for i in range(1,n+1):
        name=input(f"Enter customer {i} name :")
        age=input(f"Enter  customer {i} age")
        f.write("C_Name :"+name+"    "+"Age : "+age +"\n")
    f.seek(0)
    z=f.read()
    print(z)
    

cust_data()

