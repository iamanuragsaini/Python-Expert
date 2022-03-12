#  Initialize dictionary with default values
def check_element(employees,defaults):
    result = dict.fromkeys(employees,defaults)
    return result

if __name__ == '__main__':
    employees = ['Kelly', 'Emma']
    defaults = {"designation": 'Developer', "salary": 8000}
    result=check_element(employees,defaults)
    print(result)