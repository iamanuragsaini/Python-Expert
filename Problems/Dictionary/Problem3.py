#  Print the value of key ‘history’ from the below dict

def check_element(sampleDict):
    result = sampleDict['class']['student']['marks']['history']
    return result

if __name__ == '__main__':
    sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
    result=check_element(sampleDict)
    print(result)