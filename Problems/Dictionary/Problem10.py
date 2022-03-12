# Change value of a key in a nested dictionary
#Write a Python program to change Brad’s salary to 8500 in the following dictionary.

''' Output: {
   'emp1': {'name': 'Jhon', 'salary': 7500},
   'emp2': {'name': 'Emma', 'salary': 8000},
   'emp3': {'name': 'Brad', 'salary': 8500}
}'''

def check_element(sample_dict):
    sample_dict['emp3']['salary'] = 8500
    return sample_dict
   

if __name__ == '__main__':
    sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
    result=check_element(sample_dict)
    print(result)