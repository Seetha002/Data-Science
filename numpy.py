#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)


# In[8]:


import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr)


# In[7]:


import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr[0,1])


# In[6]:


import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr[1,-1])


# In[9]:


import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr.shape)


# In[10]:


import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])
for x in arr:
    for y in x:
        print(y)


# In[11]:


import numpy as np
arr=np.array([1,2,3,4,5])
for x in  arr:
    print(x)


# In[15]:


import numpy as np
arr1=np.array([1,2,3,4,5])
arr2=np.array([6,7,8,9,10])
arr=np.concatenate((arr1,arr2))
print(arr)


# In[22]:


import numpy as np
arr1=np.array([[1,2,3,4,5],[5,4,3,2,1]])
arr2=np.array([[6,7,8,9,10],[10,9,8,7,6]])
arr=np.concatenate((arr1,arr2),axis=1)
print(arr)


# In[20]:


import numpy as np
arr=np.array([6,5,1,3,4,2])
arr1=np.sort(arr)
print(arr1)


# In[25]:


from numpy import random
x=random.randint(100)
print(x)


# In[32]:


from numpy import random
x=random.rand()
print(x)


# In[29]:


from numpy import random
x=random.rand(3,5)
print(x)


# In[30]:


from numpy import random
x=random.randint(100,size=(3,5))
print(x)


# In[31]:


from numpy import random
x=random.rand(5)
print(x)


# In[34]:


from numpy import random
x=random.randint(5)
print(x)


# In[37]:


import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arr1=arr.reshape(4,3)
print(arr1)


# In[41]:


import numpy
import random
x=random.rand()
print(x)


# In[ ]:




