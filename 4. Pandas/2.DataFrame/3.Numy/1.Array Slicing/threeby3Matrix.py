#By slicing making Three by three matrix 
import numpy as np
matrix = np.arange(1,51).reshape(5,10)
#matrix from 2nd row to 4th row and 2nd column to 4th column
print("3 by 3 matrix = ", matrix[1:4,1:4])

print("Original Matrix = \n", matrix)