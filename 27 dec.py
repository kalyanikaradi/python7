#!/usr/bin/env python
# coding: utf-8

# In[1]:


#dict
d={}


# In[2]:


d


# In[3]:


type(d)


# In[5]:


D1={'id':1,'city':'pune','number':9689039876}


# In[6]:


D1


# In[7]:


mydict=dict()


# In[8]:


mydict


# In[11]:


mydict={'id':'4','city':'belagavi','name':'xyz'}


# In[12]:


mydict


# In[13]:


mydict.keys()


# In[14]:


mydict.values()


# In[16]:


mydict.items()


# In[18]:


mydict3={1:'one',2:'two',
         'A':['abc','xyz','pqr']}


# In[19]:


mydict3


# In[23]:


mydict3['A'][1]


# In[25]:


mydict3['A'][0]


# In[29]:


d={0:{'one':1,'two':2,'three':3},
   1:{'city':'banglaore','area':'kudulu'},
   'three':{'city':'mumbai','area':'dharavi'}}


# In[30]:


d[1]['area']


# In[35]:


#add and change
mydict1={'name':'data','id':23445,'DOB':1992,'address':'belagavi'}


# In[36]:


mydict1.update({'key':'value1'})


# In[37]:


mydict1


# In[40]:


mydict1.update({"key":"value100"})


# In[41]:


mydict1


# In[46]:


mydict1['job']='analyst'
mydict1


# In[47]:


mydict1.pop('job')
mydict1


# In[48]:


mydict1.clear()
mydict1


# In[49]:


del mydict1
mydict1


# In[ ]:




