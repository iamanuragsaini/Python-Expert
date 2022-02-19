# Find sum and avergage of list in Python
# Using simple iterative method


def sum_or_avg(list):
    count = 0
    for i in list:
        count += i
    avg = count/len(list)
    return [count, avg]


list = [2,3,5,2]
print(sum_or_avg(list))