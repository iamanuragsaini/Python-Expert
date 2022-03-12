#  Convert two lists into a dictionary

def check_element(keys,values):
    result = dict(zip(keys,values))
    return result

if __name__ == '__main__':
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    result=check_element(keys,values)
    print(result)