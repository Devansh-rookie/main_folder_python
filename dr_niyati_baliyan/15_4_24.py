"""
15 April 2024
SyntaxError
Name Error
TypeError
ValueError
ZeroDivisionError
IndentationError
IndexOutOfRange
KeyError
ModuleNotFoundError

Exception Handling Catching errors before getting to them
try and except block and else
"""


# a = int(input("Marks: "))

# if(a<0 or a>100):
#     raise ValueError("The Marks out of range.")
# else:
#     print("No Exception")
# if(marks<0):
# any error name would work here
#     raise Exception("The Marks can't be negative")
# a=0

# SyntaxError is not an Exception


# try:
#     print(a)
# except Exception as e:
#     print("NameError")
#     print("Error: ",e)
# else:
#     print("Hello World")


# a=0
# try:
#     print("HelloWorld")
#     while a<100000000:
#         a+=1
# except KeyboardInterrupt as e:
#     print("Error", e)

try:
    print(abc)
except Exception as e:
    print("Error: ",e)

# defining a wrong variable is a SyntaxError like 1a .1f something wrong that is.
# try:
#     print(a)
# except NameError:
#     print("NameError")
# except Exception as e:
#     print(e)

"""
Nested Try Blocks
"""

try:
    print(1/0)
except NameError:
    print("NameError")
except ZeroDivisionError:
    print("ZeroDivisionError")
except Exception as e:
    print(e)