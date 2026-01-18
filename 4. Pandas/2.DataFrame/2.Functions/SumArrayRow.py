#sum of Arrays Rows
import numpy as np
row_sum=np.array([[1,2,3],[4,5,6]])
print("Array Values:\n", np.sum(row_sum, axis=0)) #index 0

# Index 1
print("Array Values:\n", np.sum(row_sum, axis=1)) 

