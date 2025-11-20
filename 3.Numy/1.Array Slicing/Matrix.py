
# 3 by 3 matrix
import numpy as np
arr1=np.arange(1,101).reshape(10,10)
print("10 by 10 Array matrix ", arr1)

print("elements of array 3 by 3 matrix", arr1[0:3,0:3],"\n\n")
# OR
print("elements of array 3 by 3 matrix", arr1[1:4,1:4])
#complete row with col2 and col3 only in 2D array
print("complete row with col2 and col3 only", arr1[:,1:3]) #col3 excluded