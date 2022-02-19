# Sum of number digit in list
# using loop or str() 

def sum_of_number(list):
    sumNumber = []
    for i in list:
        sum = 0
        for digit in str(i):
            sum += int(digit)
        sumNumber.append(sum)
    return sumNumber

list = [12,13,14,15]
print(sum_of_number(list))