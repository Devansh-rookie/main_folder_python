# a= eval(input("What is a")) # input gives string if not typecasted
# b= eval(input("What is b"))
# Eval typecast into respective thing whatever was needed

# a= int(input("What is a")) # input gives string
# b= int(input("What is b"))
# int does explicit typecasting into int

a= (input("What is a:\n")) # input gives string if not typecasted
b= (input("What is b:\n"))
# or
# print(int(a)+ float (b)) # typecast here
# it will also do implicit typecasting
# if one is int and the other is string then it will give an error 
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(a+b)# a+b concatenates the two strings
# print(int(a)*b)# multiply string to print strings multiple times
# strings can't be multiplied by string
int(a)
int (b)
print("Sum of {} and {} is {}".format(a,b,int(a)+int(b)))
print("Sum of {0} and {1} is {2}".format(a,b,int(a)+int(b)))
#Format's order is 0, 1 ,2 like an array so 0 means format
#ka first element and 1 means second element and so on.....
print("Sum of {1} and {0} is {2}".format(a,b,int(a)+int(b)))
# Google Collab and stuff 

a,b = eval(input("What are a and b"))
# isme a and b both input le liye jayega

