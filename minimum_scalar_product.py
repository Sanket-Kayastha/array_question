A = [-1,5,3,6]
B = [-6,7,8,2]

A.sort()
B.sort(reverse=True)

result = 0
for i in range(len(A)):
    result += A[i]*B[i]

print(f"Minimum Scalar Product {result}")

'''..............Minimum Scalar Product......  
Sort one vector in ascending order
👉 Sort the other vector in descending order
👉 Multiply corresponding elements and sum them
....................Maximum Scalar Product.............................
Sort both vectors in the same order (either both ascending or both descending)
👉 Multiply corresponding elements and add them
'''