#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np
a=np.array([1,2,3])
print("type:%s"%type(a))
print("shape:%s"%a.shape)
print(a[0],a[1],a[2])
a[0]=5
print(a)
b=np.array([[1,2,3],[4,5,6]])
print("\nShape of b:",b.shape)
print(b[0,0],b[0,1],b[1,0])
a=np.zeros((2,2))
print("All zeros matrix:\n%s"%a)
b=np.ones((1,2))
print("\nAll one matrix:\n%s"%b)
d=np.eye(2)
print("\n identity matrix:\n%s"%d)
e=np.random.random((2,2))
print("\nRandom matrix:\n%s"%e)
print("Vectorized sum example\n")
x=np.array([[1,2],[3,4]])
print("x:\n%s)"%x)
print("Sum:%s"%np.sum(x))
print("Sum axis=0:%s"%np.sum(x,axis=0))
print("Sum axis=1:%s"%np.sum(x,axis=1))
a=np.arange(10000)
b=np.arange(10000)
dp=np.dot(a,b)
print("Dot product:%s\n"%dp)
op=np.outer(a,b)
print("\nOuter product:%s\n"%op)
ep=np.multiply(a,b)
print("\nElement wise product:%s\n"%ep)


# In[18]:


import numpy as np
x=np.array([[1,2],[3,4]])
print("Original x:\n%s"%x)
print("Transpose of x:\n%s"%x.T)


# In[22]:


from numpy import array
from scipy.linalg import svd
A=array([[1,2],[3,4],[5,6]])
print("A:\n%s"%A)
U,S,VT=svd(A)
print("\nU:\n%s"%U)
print("\nS:\n%s"%S)
print("\nV^t:\n%s"%VT)


# In[25]:


import matplotlib.pyplot as plt
plt.plot([1,2,3],[5,7,4])
plt.show()


# In[30]:


import matplotlib.pyplot as plt
x=[1,2,3]
y=[5,7,4]
plt.plot(x,y,label="First line")
x2=[1,2,3]
y2=[10,11,12]
plt.plot(x2,y2,label="Second line")
plt.xlabel("Plot number")
plt.ylabel("Important variable")
plt.title("New Graph")
plt.legend()
plt.show()


# In[ ]:




