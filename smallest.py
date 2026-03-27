N = int(input("Enter the total Number: "))
array = []
for _ in range(N):
    number = int(input())
    array.append(number)

smallest_number =1000000
for n in array:
    if n< smallest_number:
        smallest_number=n

print(f"smallest_number is {smallest_number}")