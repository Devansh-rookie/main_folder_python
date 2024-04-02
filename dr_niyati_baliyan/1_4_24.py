# class is like a capsule which contains properties and methods/ functions
# instantiate a class: create an object 

# POLYMORPHISM
# Multiple facets/ forms of a function
# Overloading and Overriding
# Dynamic Polymorphism


# class MyClass():
class MyClass:
    # x=5
    def __init__(self,x):
        self.x = x
    def __repr__(self):# returns string
        return f"x is {self.x}"
    def __str__(self): # returns string
        # return f"x is {self.x}"
        return f"x is {self.x}"
        # how to get all the properties of the class/ object similar to a function called locals()
    
    # def __add__(self, other):
    #     return self.x + other.x
    def __add__(self, other):
        ans= MyClass(self.x + other.x)
        return ans

    def square(self):
        self.x = (self.x)**2
        return self.x
    
myObject = MyClass(100) # 100 will overwrite 5 there is not point in x=5 there
# myObject2 = MyClass() # expecting one argument else error
print(myObject.x)
# print(myObject2.x)
myObject2 = MyClass(10)
print(myObject)
# print takes the class what to print
print(myObject2.x)
print(myObject2)

myObject2.x = 1000

print(myObject+myObject2)
print(myObject.square())
print(myObject)
# print(int)

# write a python class which has 2 methods get string and print string, getstring will take input of a string from the user and print string prints that string in upper case