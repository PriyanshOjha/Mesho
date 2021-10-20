#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[8]:


df1 = pd.read_csv('meesho-returns.csv')


# In[9]:


df1.head()


# In[87]:


l = df1['Order number'].tolist()


# In[61]:


df2 = pd.read_csv('ordersreturned.csv')


# In[88]:


r = df2['orders returned'].tolist()


# In[89]:


e = []
for i in l:
    if i in r:
        continue
    else:
        e.append(i)


# In[91]:


len(e)


# In[93]:


df1.head()


# In[94]:


df = pd.read_csv('GST-INVOICE.csv')


# In[95]:


df.head()


# In[109]:


s = df['Unnamed: 6'].to_list()

#df['Unnamed: 6'].to_list()[3].split(',')[-1]


# In[110]:


s = s[2:]
area = []
for i in s:
    area.append(i.split(',')[-1])


# In[111]:


area


# In[114]:


l = [0, 0]
l+area


# In[115]:


df['states'] = l+area


# In[116]:


df.head()


# In[128]:


import matplotlib.pyplot as plt
a = df['states'].to_list()
a


# In[130]:



d = {}
for i in a[2:]:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)


# In[142]:


states = list(d.keys())
counts = list(d.values())
  
fig = plt.figure(figsize = (45, 15))
 
# creating the bar plot
plt.bar(states, counts, color ='maroon',
        )


# In[ ]:




