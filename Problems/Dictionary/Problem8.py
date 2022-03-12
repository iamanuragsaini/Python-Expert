#  Rename key of a dictionary
# Write a program to rename a key city to a location in the following dictionary.

def check_element(sample_dict,key,repkey):
    keyValue = sample_dict.pop(key)
    sample_dict[repkey] = keyValue
    return sample_dict 

if __name__ == '__main__':
    sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
    key = input("Enter the key: ")
    repkey = input("Enter the key replace: ")
    result=check_element(sample_dict,key,repkey)
    print(result)