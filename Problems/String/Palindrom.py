# Program to check the string is Palindrom


def check_element(strVal):
    mid = (len(strVal)-1)//2
    start = 0
    flag = 0
    last = len(strVal)-1
    while(start <= mid):
        if(strVal[start] == strVal[last]):
            start += 1
            last -= 1
        else:
            flag = 1
            break
    if(flag == 0):
        print(f"Palindrom check successful")
    else:
        print("Not a Palindrom")
    return flag

if __name__ =='__main__':
    strVal = 'amaama'
    print(check_element(strVal))


