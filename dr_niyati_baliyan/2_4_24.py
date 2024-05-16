# getString and printString
from abc import ABC, abstractmethod
class StringAnswer:
    
    def getString(self):
        self.string = input("String is: ")
    
    def printString(self):
        print("Updated String: ",self.string.upper())

# a = StringAnswer()
# a.getString()
# a.printString()

# multiple work of init and str because that work was not done there

# a = 5
# b = 5
# print(a==b)
        
# All attributes shall be equal if the two objects are same

class Employee:
    def __init__(self, name):
        self.name = name
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __add__(self,other):
        a = Employee()
        a.name=self.name+other.name
        return a
    
    def __str__(self):
        return self.name

# emp1 = Employee("ABC")
# print(emp1.name)
# emp2 = Employee("ABC")
# print(emp2.name)
# del emp1
# del Employee
# print(emp1)

# overloading __str__ is essentially redefining it

# print(emp1)
# emp3 = emp1 # now pointing to the same Memory address so emp1==emp3
# print(emp2==emp1) # if __eq__ is not defined then it compares memory addresses

# print(emp1.name == emp2.name)

class Demo:
    _class = "MCA"
    def __init__(self,name):
        self.name = name

    def __eq__(self, other) ->bool:
        return self.name== other.name
jack = Demo("Jack")
jill = Demo("Jill")

# print(jack == jill)

# print(Demo._class)

# super.func() if we have to call the func() method of the super class if its defined in both of the class super and sub

class A:
    def func(self):
        print("superclass")
class B(A):

    def super_func(self):
        super().func()

    def func(self): # this is called overriding sub-class and super-class have methods with the same name
        print("subclass")
        super().func()

b = B()

# b.func()
# b.super_func()

# Abstract classes, Imp: Read it
# abc means abstract class
# from abc import ABC, abstractmethod 

class Polygon(ABC):# Structure
    @abstractmethod
    def sides(self): # not concrete empty
        pass
# if two parents and they have same func() then in the child which function would be called if we call super().func()
class Triangle(Polygon):
    def sides(self):
        print("3")

class Quad(Polygon):
    def sides(self):
        print("4")
T= Triangle()
T.sides()

Q = Quad()
Q.sides()

print(isinstance(Q,Quad))# isinstance(myObj, class) 
print(isinstance(Q,Triangle))
print(isinstance(Q, Polygon))
# globals() gives all the global names in the global namespace that is all the global classes and variables.
# Similar to locals() gives all the local variables in the unction its called in or maybe even in an class that is to be checked.
