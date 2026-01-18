#Find minimumvalue in the array
import numpy as np
arr = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

print("Array Values:\n", arr)

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("Array Values:\n", arr)

# Flattened index of minimum
print("Index of Minimum Value:", arr.argmin())

# Minimum value in whole array
print("Minimum Value:", np.min(arr))

# Minimum value in each column
print("Minimum Value in each column:", arr.min(axis=1))
print("Minimum Value in each column:", arr.min(axis=0))