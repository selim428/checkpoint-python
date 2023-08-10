#!/usr/bin/env python
# coding: utf-8

# In[3]:


L=[]
for i in range(2000,3200) :
    if i%7==0 and i%5!=0 :
        L.append(i)
L
    


# In[2]:


v=int(input("entrer un entier "))
fac=1
for i in range(1,n+1) :
    fac=fac*i
print(fac)


# In[6]:


n=int(input("entrer un entier "))
dict1={}
for i in range(1,n+1) :
    dict1[i]=i*i
print(dict1)






# In[3]:


m=int(input("entrer un entier "))
l=input("entrer une chaine ")
l1=""
for i in range(len(l)) :
    if i!=m :
        l1=l1+l[i]
        
print(l1)


# In[6]:


import numpy as np
t = np.array([[0,1],[2,3],[4,5]])
t_list = t.tolist()
print(t_list)







# In[12]:


import numpy as np
g=np.array([0,1,2])
f=np.array([2,1,0])
re=np.cov(f,g)
re


# In[13]:


from math import sqrt
C=50
H=30
D=input("enter 3 number seperated with a coma")
D=D.split(",")
results=[]
for i in range(3) :
    b=sqrt((2*C*int(D[i])/H))
    results.append(b)
print(f"the result is {round(results[0])},{round(results[1])},{round(results[2])}")





# In[ ]:




