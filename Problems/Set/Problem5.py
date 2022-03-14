# Remove items from the set at once

set1 = {10, 20, 30, 40, 50}
set2 = {10,20,30}
set1.difference_update(set2)
print(set1)