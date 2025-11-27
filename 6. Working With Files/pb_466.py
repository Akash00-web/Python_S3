"""
Write a python program to create and read the city.txt file in one go and print the contents on the output screen.

"""
f=open("city.txt" ,"w+")
f.write("Have a great code jearney...")
f.seek(0)
z=f.read()
print(z)
f.close()