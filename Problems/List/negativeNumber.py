# Print negative number in a list

def negative_number(list):
    count = 0
    for item in list:
        if(item<0):
            count += 1
            print(count)
    print(f"total negative number: {count}")
    return True

list = [2,3,4,5,6,7,-2,-3]
print(negative_number(list))