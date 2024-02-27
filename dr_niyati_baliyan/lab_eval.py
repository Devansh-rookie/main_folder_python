def anagram(str1,str2):
    for i in str1:
        if i not in str2:
            return False
    return True

a = input("What is string 1: ")
b = input("What is string 2: ")

if anagram(a,b):
    print("{}, {} are anagrams of each other.".format(a,b))
else:
    print("{}, {} are NOT anagrams of each other.".format(a,b))