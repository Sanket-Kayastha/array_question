array = [4,6,7,8,4,4,4,5,7,8,2,1,2,3]

freq = {}
for num in array:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] =1

print(freq)

'''Sort based on frequency (descending), then value (ascending)'''
sorted_arr = sorted(array , key=lambda x: (-freq[x], x))
print(sorted_arr)