# Astrologer's Stars

num = int(input("Enter the number:- "))
boolVal = bool(int(input("Enter the number in 0 or 1:- ")))
count = num
if(boolVal==True):
    for i in range(num+1):
        for j in range(i):
            print("*", end=' ')
        print("")
else:
    for i in range(num+1):
        for j in range(count):
            print("*",end = " ")
        print("")
        count -= 1
