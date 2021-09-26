#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


os.chdir("C:/Users/Azfa Razzaq/Videos/Captures")


# In[3]:


import pandas as pd


# In[4]:


import matplotlib.pyplot as plt


# In[5]:


import seaborn as sns


# In[6]:


data= pd.read_csv("garments_worker_productivity.csv")


# In[7]:


data


# In[8]:


data.columns


# In[9]:


#get unique values in the department column
data['department'].unique()


# In[10]:


data['department']= data['department'].str.replace('finishing ','finishing')


# In[11]:


data['department'].unique()


# In[12]:


data['department'].value_counts()


# In[13]:


data.dtypes


# In[14]:



data.info() #get information about data types and missing values


# In[15]:


#break down department in to two tables- 
#filtering the data sent in to two tables

sewing_data=data[data['department']=='sweing']
finishing_data=data[data['department']=='finishing']


# In[16]:


#plotting
fig, axes=plt.plot()


plt.show()


# In[17]:


fig, axes=plt.subplots(nrows=1,ncols=2)
(ax1,ax2)=axes

plt.show()


# In[18]:


fig, axes=plt.subplots(nrows=2,ncols=2)
(ax1,ax2), (ax3,ax4)=axes

plt.show()


# In[20]:


#ploting 

fig, axes=plt.subplots(nrows=1,ncols=2,figsize=(15,5))
(ax1,ax2)=axes
#plot a histogrom in col 1
ax1.hist(sewing_data['actual_productivity'],bins=10,alpha=0.4,label="Sewing Department")
ax1.hist(finishing_data['actual_productivity'],bins=10,alpha=0.4, label="Finishing Department")

#labelling
ax1.legend() #ask python to show the legend
ax1.set_title("Department productivity-Histogram")
ax1.set_xlabel("Productivity")
ax1.set_ylabel("count")

#draw ECDF plots using Seaborn
ax2p=sns.ecdfplot(data=data,x="actual_productivity",ax=ax2,hue="department")
ax2p.set_xlabel("Productivity")
ax2p.set_ylabel("Proportion")
ax2p.set_title("Department productivity-ECDF")

#getting median
sewing_median=sewing_data["actual_productivity"].median()
finishing_median=finishing_data["actual_productivity"].median()


#vertical and horizontal lines
ax2p.axvline(x=sewing_median,ymax=0.5,ls="--",color="black",alpha=0.5) #vertical line
ax2p.axvline(x=finishing_median,ymax=0.5,ls="--",color="black",alpha=0.5)
ax2p.axhline(y=0.5,ls="--",color="blue",alpha=0.5)

#annotations
arrow_props= dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=90,rad=10")
ax2p.annotate("$Median_{sweing}=%.4f$"%sewing_median,xytext=(0.25,0.55), xy=(sewing_median,0.5) ,arrowprops=arrow_props)
ax2p.annotate("$Median_{finish}=%.4f$"%finishing_median,xytext=(0.25,0.60), xy=(finishing_median,0.5),arrowprops=arrow_props)

plt.savefig("output")



plt.show()


# In[129]:


sewing_median


# In[171]:


finishing_median


# In[ ]:





# In[ ]:




