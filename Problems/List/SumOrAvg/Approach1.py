# Find sum and avergage of list in Python
# Using sum() or len() method

def sum_or_avg(list):
    sumElement = sum(list)
    avgElement = sumElement/len(list)
    return [sumElement, avgElement]


list = [2,3,5,2]
print(sum_or_avg(list))