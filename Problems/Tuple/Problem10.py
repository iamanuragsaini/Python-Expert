# Check if all items in the tuple are the same

tuple1 = (45, 45, 45, 45)

# for item in tuple1:
#     if item not in tuple1:
#         print("Not")
#         break
#     else:
#         print("True")

result = all(item==tuple1[0] for item in tuple1)
print(result)