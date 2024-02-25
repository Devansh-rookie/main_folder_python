class Employee:
    num_of_emp= 0
    raise_amount= 1.04
    # this is known as a class variable this variable would be used by all the instances of the class if nothing else is specified by the user/ programmer to access it in function self.var_name would be used as it still can be changed for a specific instance of a class for e.g. emp1 and so on and if the class variable like Employee.raise_amount is changed instead of the instance variable emp1.raise_amount the variable would be changed in the entire class and all instances. While if the change is wrt a specific instance. self.var_name would use the instance variable


    # regular class methods automatically take self as the first argument we call it self by convention

    # regular methods/functions take self as the argument automatically and class methods automatically take the class as it and in the meanwhile static methods don't take any of them
    
    def __init__(self, fname, lname, pay):
        # here self means while initializing the classes emp1= Employee("Name","Last Name", 50000) self automatically does it
        self.first = fname
        # self means the thing that is itself, fname would be the first argument that would be passed then lname and pay
        self.last = lname
        self.pay = pay # can be same name or different
        self.email = fname+'.'+lname + "@work.com"
        
        Employee.num_of_emp+=1
        # here every time a new object is initialized the class variable would be changed for all instances as all are inheriting the same thing there is no instance or self.var assigned like that.

    
    # def fullname():
    # # here its an error as self was not passed so it will give a TypeError: fullname() takes 0 positional arguments but 1 was given // that is self was automatically give but fullname wasn't taking any arguments
    #     return "{0} {1}".format(self.first, self.last)
    
    def fullname(self):
        return "{0} {1}".format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int(self.pay * 1.04)
        # here instead of 1.04 which means a fixed 4% increase we should use another variable which can also be changed later.
        self.pay = int(self.pay * self.raise_amount)
        #using int to make it a whole number instead of the float it would make
    def print_vals(self):
        print(self.fullname(), self. email, self.pay, sep="\n")
    @classmethod
    # this @ symbol and the thing typed is a decorator
    #this is a class method which takes the first argument as the class itself, by convention we usually take cls as that argument
    def set_raise_amt(cls, amount):
        cls.raise_amount= amount

    @classmethod
    def make_object_from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        # this is the unpacking of the list in first last and pay
        # return Employee(first, last, pay)
        return cls(first, last, pay)
        # both of them can be used as cls is Employee itself as its a class method.

emp1 = Employee("Bill", "Gates", 100000)

emp2 = Employee("Steve", "Jobs", 100000)
emp3 = emp1 # same pointing if change in emp1 then it would reflect in emp3 

# emp3 is not initialized so num_of_emp+=1 would not be done

print(emp1,emp2,emp3)

print("\n")
print(Employee.num_of_emp) # incremented 2 times by now
print("\n")


# print(emp1.fullname(),"\n", emp1.email,sep="")
print(emp1.fullname(), emp1.email,sep="\n")
# emp4= Employee.__init__("Yes", "No", 100000)

emp4 = Employee("Yes", "Yes", 100000)

print(Employee.fullname(emp4),"\n", emp4.email,sep="")

print(emp1.__dict__)
print("Employee.__dict__",'\n',Employee.__dict__)

print("\n")

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print("\n")

emp1.raise_amount = 1.10

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print("\n")

Employee.raise_amount = 1.05

print(Employee.raise_amount)
print(emp1.raise_amount)# the raise_amount remained 1.10 for this as it was changed after initializing the object it is somewhat like over writing that
#it has been changed in its name space to 1.1

print(emp2.raise_amount) # it was changed to 1.05 and its inheriting the same value that is the Employee.raise_amount 
print("\n")
print(Employee.num_of_emp) # incremented 3 times by now

# there are both class variables and class methods
# and static methods and static variables


Employee.set_raise_amt(1.04)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print("\n")


emp = "John-Doe-70000"
new_from_string = Employee.make_object_from_string(emp)
Employee.print_vals(new_from_string)
