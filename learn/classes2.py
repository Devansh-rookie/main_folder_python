import datetime

class Employee:
    num_of_emp= 0
    raise_amount= 1.04
    # this is known as a class variable this variable would be used by all the instances of the class if nothing else is specified by the user/ programmer to access it in function self.var_name would be used as it still can be changed for a specific instance of a class for e.g. emp1 and so on and if the class variable like Employee.raise_amount is changed instead of the instance variable emp1.raise_amount the variable would be changed in the entire class and all instances. While if the change is wrt a specific instance. self.var_name would use the instance variable


    # regular class methods automatically take self as the first argument we call it self by convention

    # regular methods/functions take self as the argument automatically and class methods automatically take the class as it and in the meanwhile static methods don't take any of them

    # if we don't access the instance of the class or the class itself in any method the function should Ideally be a static method

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
    
    @staticmethod
    def is_workday(day):
        if day.weekday()== 5 or day.weekday()==6:
            return False
        return True


# here the class developer is inheriting all the methods and functionalities from the class Employee just put the class from which you want to inherit from in the bracket then use it as a normal class

class Developer(Employee):
    raise_amount = 1.10
    # this will only affect the developer subclass and not any other instance of the Employee class whatsoever and the data resolution order is 1. developer then Employee then bulletins.object its basically re writing anything we want like the raise_amount here is rewritten here for the developer class.
    
    # if we want to handle more parameters then we already have for the super class we can just use super() or the class names init method then write a new init method for the subclass

    def __init__(self, fname, lname, pay, prog_lang):
        # this is one way of doing it 
        super().__init__(fname, lname, pay) 
        # this will basically run the Employee class' __init__ method and then the control would come back here

        # another is to write the entire thing

        # Employee.__init__(self, fname, lname, pay)

        #now we can just add normal stuff in the thing
        self.prog_lang = prog_lang

class Manager(Employee):
    # we usually don't put mutable datatypes as default value
    # here employee is a list which contains objects of Manager and Developer class
    def __init__(self, fname, lname, pay, employee= None):
        super().__init__(fname, lname, pay) # first it will call the Employee class' __init__ method then it will go on to the rest of the manager class' __init__ method.
        # with None always "is" is used instead of == i.e. equality operator
        if employee is None:
            self.employee= []
        else:
            self.employee = employee
    
    def add_emp(self, emp):
        if emp not in self.employee:
            self.employee.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employee:
            self.employee.remove(emp) # .remove(val) removes the first occurrence of the val
    
    def print_emp(self):
        for emp in self.employee:
            print("-->",emp.fullname())


dev_1= Developer("ABC", "123", 100000, "Python")
dev_2 = Developer("Test", "Employee", 100000, prog_lang="C++")

print(dev_1.email)
print(dev_2.email)

print("\n")

# print(help(developer))

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print("\n")

print(dev_1.prog_lang)
print(dev_2.prog_lang)

print("\n")

mgr_1 = Manager("Sue", "Smith", 120000, [dev_1])

print(mgr_1.email)
mgr_1.print_emp()

mgr_1.add_emp(dev_2)

print(mgr_1.email)
mgr_1.print_emp()


mgr_1.remove_emp(dev_1)

print(mgr_1.email)
mgr_1.print_emp()

# isinstance() is a builtin function which tells if, object is an instance of the particular class, if a super class is checked with an instance of a subclass then it will return True as well e.g. print(isinstance(mgr_1, Employee))

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Developer))
print(isinstance(mgr_1, Employee))

# issubclass() tells if a class is a subclass of that particular class

print(issubclass(Manager, Employee))# Manager is a subclass of Employee
print(issubclass(Manager, Developer))# Manager is not a subclass of Developer
print(issubclass(Employee, Employee)) # this will return True subclass of itself
print(issubclass(Employee, Manager)) # Employee is not a subclass of Manager

