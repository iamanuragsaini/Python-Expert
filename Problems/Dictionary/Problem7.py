#  Check if a value exists in a dictionary

def check_element(sample_dict,value):
    res = ''
    if value in sample_dict.values(): 
        res = f'{value} is present'
        return res
    else:
        res = f'{value} is not present'
        return res


 
if __name__ == '__main__':
    sample_dict = {'a': 100, 'b': 200, 'c': 300}
    value = int(input("Enter the number: "))
    result=check_element(sample_dict,value)
    print(result)