#  Delete a list of keys from a dictionary

def check_element(sample_dict,keys):
    result = {sample_dict.pop(k) for k in keys}
    return sample_dict

if __name__ == '__main__':
    sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
    }
    keys = ['name','salary']
    result=check_element(sample_dict,keys)
    print(result)