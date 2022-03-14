# Update set1 by adding items from set2, except common items

import re


def check_element(set1,set2):
    set1.symmetric_difference_update(set2)
    return set1

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

result = check_element(set1,set2)
print(result)