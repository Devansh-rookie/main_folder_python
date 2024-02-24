# start_fee = 10000
# rate = 5.00
# fee_5=10000
# for i in range(1,6):
#   fee_5=fee_5+fee_5*rate/100
# print("5 Years from now: ", fee_5)

# _4_year= fee_5
# sum=0
# for i in range(1,5):
#     _4_year += _4_year*rate/100
#     sum += _4_year
# print("The total fees: ", sum)

count =0
for i in range(100,1001):
    if(i%30==0): # or directly check with 30
        if(count%10!=0):
            print(i,end=" ")
            count+=1
        else:
            if count!=0:
                print("\n")
            print(i,end=" ")
            count+=1