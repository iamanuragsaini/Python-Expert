#  Create a dictionary by extracting the keys from a given dictionary

def check_element(sample_dict,keys):
    result = {k:sample_dict[k] for k in keys}
    return result

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