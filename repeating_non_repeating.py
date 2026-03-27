array = [4,8,7,9,6,2,1,1,3,4,8,6,7]

freq = {}
for num in array:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

repeating = []
non_repeating = []
for key , value in freq.items():
    if value>1:
        repeating.append(key)
    else:
        non_repeating.append(key)

print(f"Repeating element is: {repeating}")
print(f"Non Repeating element is : {non_repeating}")