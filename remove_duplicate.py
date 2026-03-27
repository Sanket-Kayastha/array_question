array = [1,5,6,5,4,8,9,2,1,6]

# r_dup = list(set(array))
# print(r_dup)
unique = []
for num in array:
    if num not in unique:
        unique.append(num)

print(f"Unique element is : {unique}")