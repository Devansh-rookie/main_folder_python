# assuming bin is in str
def convertToDecimal(bin):
    val =0
    for i in range(len(bin)):
        val += int(bin[-i-1])*(2**(int(i)))
    return val

a = input("Input: ")
b = a.split(",")
for i in b:
    if(convertToDecimal(i)%5==0):

        print(f"{i} is divisible by 5.")