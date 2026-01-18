#Arrange Function for how many elements by using
#Reshape for 10 row and 10 columns
import numpy as np
arr1=np.arange(1,101).reshape(10,10)
print("10 by 10 Array matrix ", arr1)

#find max (Index,column)
print("Max value at[ind,col]=[0,0] ", arr1[0,0])
print("Max value at[ind,col]=[0,0] ", arr1[0,0].ndim) #dimension
#first row all columns
print("First row all columns ", arr1[0,])

#first column all rows
print("First column all rows ", arr1[:,0])

#single column two dimension arr1[:,0:1])
print("Single column two dimension ", arr1[:,0:1])
#for finding its dimension
print("Dimension of single column two dimension ", arr1[:,0:1].ndim)