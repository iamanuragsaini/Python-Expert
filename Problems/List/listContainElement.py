# check - 3 consecutive element in a list

def check_element(list):
    for i in range(len(list)-2):
        if list[i] == list[i+1] and list[i+1] == list[i+2]:
            print(list[i])
    return True
       

list = [1,2,2,2,3,4,4,4,6,3,7,7,9]
print(check_element(list))