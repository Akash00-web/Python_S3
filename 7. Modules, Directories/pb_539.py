"""
Stacks and Queues. Write a class SQ that defines a data structure that can behave as both a queue (FIFO) or a stack (LIFO),
There are five methods that should be implemented:
1.make a constructor with a valid parameter
2.shiŌ() returns the first element and removes it from the list. Also, use the custom(raise) excepƟon in this method.
3.unshiŌ() "pushes" a new element to the front or head of the list
4.push() adds a new element to the end of a list
5.pop() returns the last element and removes it from the list
6.remove() returns the maximum element of the list and removes it from the list.
7.Create the object and call all methods of the SQ class.

"""


    
class SQ:
    
    def __init__(self,l):
        self.l=l
        print(l)
        
    def shift(self):
        try:
            if len(l)==0:
                raise Exception("Empty")
        except Exception as e:
            print(e)
        else: 
            l.pop(0)
            print("SHIFT ",l)

       
    def unshift(self):
        n=int(input("NEW ELEMENT at start"))
        l.insert(0,n)
        print("UNSHIFT " ,l)
        
        
    def push(self):
        n=int(input("NEW Element at end"))
        l.append(n)
        print( "PUSH ",l)
        
    def pop(self):
        l.pop()
        print( "POP ",l)
        
        
    def remove(self):
        maxi=max(l)
        l.remove(maxi)
        print("MAx ",maxi)
        print("MAX REMOVEd ",l)

l=[1,2,3,4,5,6,7,8,9,10]
s=SQ(l)
s.shift()
s.unshift()
s.push()
s.pop()
s.remove()
