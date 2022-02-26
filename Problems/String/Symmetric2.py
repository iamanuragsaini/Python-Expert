# check string is Symmetric or not

def check_element(string):
    n = int(len(string))
    if n%2 == 0:
        mid = n // 2
    else:
        mid = n//2 + 1
    start = 0
    last = mid
    flag = 0

    while(start < mid and last < n):
        if(string[start] == string[last]):
            start += 1
            last += 1
        else:
            flag = 1
            break

    if flag == 0:
        print("Symmetric")
    else:
        print("Not Symmetric")

string = 'amaama'
check_element(string)