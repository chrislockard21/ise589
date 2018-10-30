# 1
# Make a jupyter notebook

import numpy as np
aVec = np.random.randint(0,100,20)
b = np.random.rand()*100
aV_ABC = np.absolute(aVec - b)

minval = aV_ABC.min()
index = np.where(aV_ABC == minval)

print(aVec[index])


# 5
a = np.random.randint(10,100,20)
a[a-a.mean() < 0] = 0
print(a)


# 6
x = np.arange(25).reshape(5,5)
x[:] = 100
x[1:-1, 1:-1] = -1
print(x)


# 16
a = np.random.randint(1,100,10)[np.newaxis]
B = np.random.randint(1,100,50).reshape(10,5)
print(B-a.T)
