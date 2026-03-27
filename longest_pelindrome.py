arr = [121,123,454,6767,9999]

longest = ""
for num in arr:
    s = str(num)
    print(s[::-1])
    if s == s[::-1]:
        if len(s)>len(longest):
            longest = s

print("Longest Palindrome: ", longest)