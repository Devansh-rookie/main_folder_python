class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first +"."+ last +"@work.com"
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    @property # so we don't need to use setters and getters everywhere
    def email(self): # but if we don't use the @property here email would be function everywhere while with that decorator we would have it called like a function but accessed like a property
        # return f"""{self.first}.{self.last}@work.com"""
        return "{}.{}@work.com".format(self.first,self.last)
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last
        # here it completely changes the first and last name to change the fullname as its a property so can't be changed directly
        # it works on equation of it
    
    @fullname.deleter
    def fullname(self): # no argument
        print("Deleted Name")
        self.first = None
        self.last = None
        # completely changes it

emp_1 = Employee("John", "Smith")
emp_1.first = "Jim"

print(emp_1.first)
print(emp_1.email) # email is not changed as it was initialized with init while fullname is updated as its a function and its called later
# so getter and setter is better in languages like Java
#here 
# emp_1.fullname="Corey Schafer"
# can't be done as it is a property now
# AttributeError: property 'fullname' of 'Employee' object has no setter

emp_1.fullname="Corey Schafer"

print(emp_1.fullname)
print(emp_1.first)

del emp_1.fullname
print(emp_1.fullname) # None None