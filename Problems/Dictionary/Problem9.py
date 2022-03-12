# Get the key of a minimum value from the following dictionary

def check_element(sample_dict):
    allKeys = list(sample_dict.keys())
    allValues = list(sample_dict.values())
    minValue = min(allValues)
    idx = allValues.index(minValue)
    result = allKeys[idx]
    return result

# Other Method

def chk_elm(sample_dict):
    value = min(sample_dict.values())
    for k,v in sample_dict.items():
        if v == value:
            return k

if __name__ == '__main__':
    sample_dict = {'Physics': 82,'Math': 65,'history': 75 }
    result=chk_elm(sample_dict)
    result=check_element(sample_dict)
    print(result)