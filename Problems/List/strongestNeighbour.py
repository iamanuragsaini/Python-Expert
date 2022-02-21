# Program to find the strongest neighbour

def check_element(list):
    arr = []
    for item in range(len(list)-1):
        r = max(list[item], list[item+1])
        arr.append(r)
    for i in arr:
        print(i)
    return arr

    
       

list = [1,2,2,3,6,3,7,9]
print(check_element(list))