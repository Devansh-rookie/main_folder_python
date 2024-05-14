'''Question 1'''

def convertToDict(s: str):
    d = dict()

    a = s.split(" ")
    for i in a:
        d[i] = len(i)
    return d

s = input(" What is the sentence: ")
d = convertToDict(s)
print("The dictionary is:\n",d)
print("Word\tLength")
for i in d:
    print(f"{i}\t{d[i]}")


'''Question 2'''

# def fib(n):
#     if(n==1 or n==2):
#         return n-1
#     return fib(n-1)+fib(n-2)

# n = int(input("What is n: "))
# flag = False
# i=1
# arr = []
# while(fib(i)<=n):
#     arr.append(fib(i))
#     i+=1
# # print(arr)

# if(n in arr):
#     print(f"{n} is in Fibonacci series at {len(arr)}.")
# else:
#     print(f"{n} is not in Fibonacci series.")


# d = {1:2, 3:4}
# d.pop(3)
# d.popitem()
# d = type((1,2))
# print(d)
# a=[1,2,4]
# print(a.index(1))
# a ="abc"
# print(a.index("b"))

# class asdff():
#     pass
