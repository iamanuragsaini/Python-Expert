#  Merge two Python dictionaries into one

def check_element(keys,values):
    dict1.update(dict2)
    return dict1

if __name__ == '__main__':
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    result=check_element(dict1,dict2)
    print(result)