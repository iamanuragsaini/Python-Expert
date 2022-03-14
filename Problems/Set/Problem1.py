# Add a list of elements to a set

def update_element(sample_set, sample_list):
    sample_set.update(sample_list)
    return sample_set

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
result = update_element(sample_set,sample_list)
print(result)