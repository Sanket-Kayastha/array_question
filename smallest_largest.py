array = [4,5,8,9,6,5,1,63]

smallest_element = 1000
largest_element =0
for n in array:
    if n>largest_element:
        largest_element = n
    elif n<smallest_element:
        smallest_element = n

print(f"Largest Element is {largest_element}")
print(f"Smallest Element is {smallest_element}")
