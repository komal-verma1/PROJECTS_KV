#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install numpy


# In[4]:


pip install pandas


# In[5]:


pip install seaborn


# In[6]:


pip install matplotlib


# In[8]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[11]:


df=pd.read_csv("Students.csv.csv")
print(df.head())


# In[12]:


df.describe()


# In[13]:


df.info()


# In[14]:


df.isnull().sum()


# # dropping unnamed columns
# 
# 

# In[18]:


df=df.drop("Unnamed: 0", axis= 1)
print(df.head())


# # Gender Distribution

# In[31]:


plt.figure(figsize= (4,5))
ax= sns.countplot(data= df, x= "Gender")
ax.bar_label(ax.containers[0])
plt.title("Gender Distribution")
plt.show()


# In[ ]:


# From the above chart we have analyzed that the number of females in the data is more than number of males


# In[26]:


gb= df.groupby("ParentEduc").agg({"MathScore":'mean', "ReadingScore":'mean', "WritingScore":'mean' })
print(gb)


# In[33]:


sns.heatmap(gb, annot= True)
plt.title("Relationship between Parent's Education and Student's Score")
plt.show()


# In[ ]:


# From the above chart we have concluded that the education of the parents have a good impact on their scores


# In[29]:


gb1= df.groupby("ParentMaritalStatus").agg({"MathScore":'mean', "ReadingScore":'mean', "WritingScore":'mean' })
print(gb1)


# In[34]:


sns.heatmap(gb1, annot= True)
plt.title("Relationship between Parent's Marital Status and Student's Score")
plt.show()


# In[ ]:


# From the above chart we have concluded that there is no/ negligible impact on the 
#student's score due to their parent's marital status


# In[35]:


sns.boxplot(data= df, x="MathScore")
plt.show()


# In[36]:


sns.boxplot(data= df, x="ReadingScore")
plt.show()


# In[37]:


sns.boxplot(data= df, x="WritingScore")
plt.show()


# In[38]:


print(df["EthnicGroup"].unique())


# # Distribution of ethnic groups

# In[40]:


groupA= df.loc[(df['EthnicGroup'] =="group A")].count()
groupB= df.loc[(df['EthnicGroup'] =="group B")].count()
groupC= df.loc[(df['EthnicGroup'] =="group C")].count()
groupD= df.loc[(df['EthnicGroup'] =="group D")].count()
groupE= df.loc[(df['EthnicGroup'] =="group E")].count()


# In[49]:


l= ["group A", "group B", "group C", "group D", "group E"]
mlist= [groupA["EthnicGroup"], groupB["EthnicGroup"], groupC["EthnicGroup"], groupD["EthnicGroup"], groupE["EthnicGroup"]]
plt.pie(mlist, labels=l, autopct= "%1.2f%%")
plt.title("Distribution of Ethnic Groups")
plt.show()


# In[ ]:




