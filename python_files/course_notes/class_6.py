
# coding: utf-8

# ## My First Numpy Code Exercises

# In[7]:


import numpy as np


# ## Create a numpy 1D = vector

# In[8]:


a = np.array([1,2,3,4,5,6])
a


# In[13]:


# 5 equal spaces between 10 and 100
b = np.linspace(10, 100, 5)
b


# In[15]:


# Start, end, incriment
a = np.arange(-5, 5, 0.5)
a


# In[17]:


# Random numbers between 0 and 1
b = np.random.rand(100)
b


# In[20]:


# Mean variance and std
b.mean(), b.var(), b.std()


# In[21]:


# Column vector
acol = np.array([[1],[2],[3]])
acol


# In[22]:


# Transpose
acol.T


# ## Creating Multi-D Arrays (Matrices)

# In[23]:


A = np.array([[1,2,3],[4,5,6],[7,8,9]])
A


# In[27]:


# Matrix generation
A = np.arange(100).reshape(10,10)
A


# In[28]:


A.T


# In[30]:


# Creates single list from matrix
A.flatten()


# In[34]:


# Will try to combine the two matricies
ix, iy = (4,2)
x = np.linspace(0,1,ix)
y = np.linspace(0,1,iy)
(xv, yv) = np.meshgrid(x,y)
xv, yv


# In[35]:


A = np.arange(64).reshape(8,8)
A


# In[36]:


np.diagonal(A)


# In[38]:


# k lets you get the specific diagonal you want
np.diag(np.diagonal(A), k=1)


# In[41]:


x = np.arange(10)
y=x
y


# In[42]:


x[0] = 10


# In[43]:


x
y=x


# In[44]:


y[0]


# In[45]:


y = np.copy(x)
y


# ## Slicing 1D and 2D Arrays

# In[46]:


# Slicing 1D arrays
a = np.arange(100)
a[5:35]


# In[47]:


# Slicing 2D arrays
A = np.arange(64).reshape(8,8)
A[1:,5:]


# In[48]:


A[1:,5:]=0
A


# In[49]:


A = np.arange(64).reshape(8,8)


# In[52]:


B = np.triu(A) # Use tril for lowwer triangle


# In[54]:


B.size, B.shape, B.ndim


# ## Array Operations

# In[59]:


a = np.arange(10).reshape(10,1)
b = np.arange(5).reshape(5,1)


# In[60]:


a*2


# In[62]:


a + b.T


# In[64]:


A = np.random.randn(25).reshape(5,5)
B = np.random.randn(25).reshape(5,5)
A, B


# In[65]:


A + B


# In[66]:


np.dot(A, B)


# In[67]:


a = np.random.randn(25)
b = np.random.randn(25)
np.dot(a, b)


# In[69]:


C=A*B
C.size


# In[70]:


A = np.arange(100).reshape(10,10)
A


# In[71]:


np.hsplit(A,2)


# In[72]:


np.vsplit(A, 5)


# In[74]:


a = np.array([0,1,0])
b = np.tile(a,100)
b


# In[75]:


A = np.arange(36).reshape(6,6)
B = np.tile(A, 5)
B


# In[76]:


B.size


# In[78]:


B.shape


# In[83]:


A = np.random.randn(9).reshape(3,3)
A


# In[84]:


A.sort()
A


# In[87]:


B = np.random.randn(16).reshape(4,4)
np.sort(B, axis=0)


# In[89]:


b = np.random.randn(16)
np.sort(b)[-5:]


# In[92]:


np.max(b), np.min(b)


# In[103]:


# Write a python program to find the most frequent value in a rondomly
# generated array with 30 elements
a = np.random.randint(0, 20, 30)
np.bincount(a).argmax()


# In[106]:


# x + 2y + z = 2, 2x + 6y + z = 7, x + y + 4z = 3. Solve for x, y and z
A = np.array([[1,2,1],[2,6,1],[1,1,4]])
B = np.array([2,7,3])
result = np.linalg.solve(A,B)
result


# In[107]:


# Checking the result and you should get B back
np.dot(A, result)


# In[108]:


np.allclose(np.dot(A, result),B)


# In[114]:


# Boolean indexing
A = np.random.randn(25).reshape(5,5)
A


# In[115]:


A[A-A.mean()>0]


# In[116]:


# Write a numpy program to find the closest value in an array to a randomly generated scalar value
A = np.array([3,4,55,36,77,88,34,26,59,67])
B = np.random.randint(100)
B


# In[120]:


index = np.abs(A-B).argmin()
A[index]


# In[121]:


a = np.arange(10)
a


# In[122]:


np.sin(a)


# In[128]:


# Write a python program to add the $ sign to every element in an array
# Use of universal funcs = decorator functions
@np.vectorize
def add_dollar(arr):
    dollar='$'
    newarr = dollar + str(arr)
    return newarr


# In[129]:


a = np.arange(10)
add_dollar(a)

