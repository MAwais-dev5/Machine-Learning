#reshape Change 1d into 2d or 3d
import numpy as np
Arr_1d= np.arange(1,13)
print("arrange function with 1D array", Arr_1d)
Arr_d2=Arr_1d.reshape(3,4)
print("Reshape 1D into 2D",Arr_d2)

Arr_d3=Arr_1d.reshape(2,3,2)
print("Reshape 1D into 3D",Arr_d3)

#Or
ar=np.arange(1,25).reshape(4,6)
print("reshaped array",ar)