array = [4,5,8,9,6,2,1,1,2,3,6,4]

# distinct = []
# for num in array:
#     if num not in distinct:
#         distinct.append(num)

# print(f"distinct element is {distinct}, lenght of distinct element is: {len(distinct)}")
distinct = {}
for num in array:
    if num in distinct:
        distinct[num] +=1
    else:
        distinct[num] = 1

print(distinct)
print(len(distinct))