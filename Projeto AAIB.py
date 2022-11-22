#!/usr/bin/env python
# coding: utf-8

# In[65]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[66]:


df = pd.read_csv("Data/EEG.machinelearing_data_BRMH.csv")


# In[104]:


df


# In[113]:


for el in df.columns:
    print(el)


# In[68]:


ser = df.duplicated()
total = 0
for i, el in ser.iteritems():
    if el:
        total += 1
print('Duplicated values: ' + str(total))


# In[90]:


df['main.disorder'].value_counts()


# In[107]:


disorder = 0 
healthy = 0
for i, el in df['main.disorder'].iteritems():
    if el != "Healthy control":
        disorder += 1
    else: 
        healthy += 1

print('Disorder: {disorder}\nHealthy: {healthy}'.format(disorder=disorder, healthy=healthy))


# In[70]:


df['main.disorder'].unique()


# In[71]:


df['specific.disorder'].value_counts()


# In[117]:


plt_ = df['main.disorder'].value_counts().sort_index().plot(kind='bar', title='')
plt_.set_title('Main Disorder Samples')
#plt_.set_xlabel('Main Disorder')
plt_.set_ylabel('No. Samples')


# In[116]:


plt_ = df['specific.disorder'].value_counts().sort_index().plot(kind='bar', title='')
plt_.set_title('Specific Disorder Samples')
#plt_.set_xlabel('Specific Disorder')
plt_.set_ylabel('No. Samples')


# In[132]:


binary_class = ['Disorder', 'Healthy control']
samples_count = [disorder, healthy]

plt.bar(binary_class, samples_count, color='blue', width=0.5)
plt.xticks(binary_class)
plt.ylabel('No. Samples')
#plt.xlabel('Class')
plt.title('Binary Classification')
plt.show()


# In[136]:


fig1, ax1 = plt.subplots()
ax1.pie(samples_count, labels=binary_class, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


# In[ ]:




