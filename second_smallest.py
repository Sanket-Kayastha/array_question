array = [3,2,5,2,4,4,5,9,7,6,45]

un_array = list(set(array))
un_array.sort()
print(un_array)
print(f"Second smallest element is {array[1]}")