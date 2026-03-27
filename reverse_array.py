array = [4,8,9,6,3,2,7]
reverse_array = []

# reverse = array[::-1]
# print(reverse)

start = 0
end = len(array)-1

while start<end:
    array[start] , array[end] = array[end], array[start]

    start+=1
    end -=1

print(f"Reversed array is {array}")