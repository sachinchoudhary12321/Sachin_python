import numpy as np
a1=np.array([[1,2,3],[4,5,6]])
a2=np.array([10,12,13,14,15,16]).reshape(2,3)
# along the rows
a3=np.concat((a1,a2),axis=0)
print(a3)
# along the columns
a3=np.concat((a1,a2),axis=1)
print(a3)
