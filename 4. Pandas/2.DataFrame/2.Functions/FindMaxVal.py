#Find maximumvalue in the array
import numpy as np
arr = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

print("Array Values:\n", arr)

print("Index of Maximum Value:", arr.argmax())  # flattened index
print("Maximum Value:", arr.max())              # actual maximum value
#maximum value in each row by index
print("Maximum Value in each row:", arr.max(axis=1))
