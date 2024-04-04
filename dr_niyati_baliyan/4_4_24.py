
class C:
    name ="John"
    def anyMethod(self):
        print("Printing from C")
    @classmethod
    def printing(cls):
        print(cls.name)

    def printing_self(self):
        print(self.name)

    def fun(self):
        print("From C")

# c = C()
# c.printing()
# print(c.name)
# c.printing_self()

class A(C):
    def fun(self):
        print("Printing from A")

class B(A):
    def fun(self):
        print("Printing from B")
        # super().fun()

b = B()

# b.fun()
# print(b)
# print(B)
# del b 
# print(b)
print(isinstance(b,B))
print(issubclass(B,A))
print(issubclass(B,C))

class Person:
    def __init__(self,fname, lname) -> None:
        self.fname =fname
        self.lname = lname
    def print_name(self):
        return (f"Welcome, {self.fname} {self.lname}")

# person = Person("John", "Nash")
# person.print_name()

class Student(Person):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.year = year
    def welcome1(self):
        print(f"Welcome, {self.fname} {self.lname} to the class of {self.year}.")
    
    def welcome2(self):
        print(super().print_name() + f" to the class of {self.year}.")
student = Student("John", "Doe", 1982)
student.print_name()
student.welcome1()
student.welcome2()