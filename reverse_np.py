import numpy as np
x=np.arange(1,10)
p=np.size(x)

print(x)
n=0
ar=np.empty(p,dtype=int)
for z in x:
        ar[-1-n]=z
        n+=1
print(ar)      

