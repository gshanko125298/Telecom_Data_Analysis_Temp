#!/usr/bin/env python
# coding: utf-8

# # Predicting on telecom business profitability 

# Introduction 
# The project proposes providing an advices for the investor who went to invest on telecommunication. The investor went to have profit of 25% within 6 months. The advices provided by analyzing the given telecom dataset.  Based on the detail telecom dataset we helped the investor weather to purchase  the company or not. As a business rule of the company this delivery company and ramp up profits by through focusing on the most profitable aspect of the business.
# 
# Objective of the project :
# the project aims to achive or privided best advices for the invester thorugh performing the follwing activieties 
#         1. User Overview analysis 
#         2.User Engagement analysis
#         3. Experience Analytics
#         4. Satisfaction Analysis
# with in each parts of the above activites there are diffrent sub-Activities 
# the following shows each detail activites of that had been taken on data to clean,transfer, exploar modeland predication analysis 

# ### part I. Data cleaning , transfer and extraction

# The main purpose of the project is to provide and advdice for invester based on the given dataset. to ensure the profitability 
# of the business. To perfoem that the main and first activity is looking to the data , cleaning data,droping unwanted raw and 
# column if it esusts , substituting the missed value ....
# the follwing activites provide that insght for the user 

# ##### Data cleaning

# Data cleaing stars form uploading Data

# In[75]:


import pandas as pd
import numpy as np
from IPython.display import Image


# In[76]:


tele=pd.read_csv(r"C:\Users\Genet Shanko\Desktop\Week_1_challange\Week1_challenge_data_source(CSV).csv",na_values=['numeric_only',None])
tele.head()


# The above telocm data have 5 rows with 55 column. the follwoing data shows the number of column avialbe in the dataset

# In[77]:


tele.columns.tolist()


# to have general information about the dat frame

# In[112]:


tele.info()


# In[78]:


len(tele.columns)


# In[79]:


totalcells= len(tele)
totalcells


# To exploer the types and number of data points, the follwoing code may support

# In[80]:


tele.shape


# In[81]:


print(f" There are {tele.shape[0]} rows and {tele.shape[1]} columns")


# To identifay the null value within the dataset 

# In[82]:


tele.isnull()


# To explor the number of the null value in each column and totol null value as a whole 

# In[83]:


tele.isnull().sum()


# In[84]:


tele.isnull().sum().sum()


# ##### Handling missing values 

# Before handling the missing value , let us check the data distrbusion 

# In[96]:


missingCount = tele.isnull().sum()
missingCount


# In[97]:


totalMissing = missingCount.sum()
totalMissing


# In[98]:


totalCells = np.product(tele.shape)
totalCells 


# In[99]:



print("The Telecome dataset contains", round(((totalMissing/totalcells)*100), 2), "%", "missing values.")


# In[100]:


tele.isna().sum()


# In[101]:


tele.skew(axis=0)


# In[ ]:


To veiw the data types of each of the 


# In[95]:


tele.dtypes


# In[103]:


import seaborn as sns
sns.displot(data=tele, x=tele['Handset Manufacturer'])


# the following figure shows the number of handset manfacturer  and the number appratus used by custmers

# In[109]:


tele['Handset Manufacturer'].hist()


# In[ ]:


tele['Handset Type'].hist()


# to have the gneral discription of the dataset 

# In[ ]:





# In[ ]:


def find_min_max_in(df, col):
    """
    The function takes in a column and returns the top 5
    and bottom 5 movies dataframe in that column.
    args:
        col: string - column name
    return:
        info_df: dataframe - final 5 movies dataframe
    """
    top = df[col].idxmax()
    top_df = pd.DataFrame(df.loc[top])
    bottom = df[col].idxmin()
    bottom_df = pd.DataFrame(df.loc[bottom])
    info_df = pd.concat([top_df, bottom_df], axis=1)
    return info_df
find_min_max_in(movies_df, 'budget')


# Drope single value column

# In[113]:


tele_data=tele.copy()
single_value_columns = pd.DataFrame(tele_data.apply(lambda x: len(x.value_counts()), axis=0), columns=['SingleValueColumn'])
drop_single_value_columns = list(single_value_columns.loc[single_value_columns['SingleValueColumn']==1].index)
print('Columns which have just a single value => \n\n' + str(drop_single_value_columns))
tele.drop(drop_single_value_columns, axis=1, inplace=True)
print('\n\nRemaining Columns => ' + str(len(tele.columns)))


# to count  duplicated column use 

# In[117]:


# Count of duplicates
tele.duplicated().value_counts()
# Drop duplicates
tele_dup=tele.drop_duplicates(keep='first', inplace=True)
#tele.drop_duplicates(subset=['custem_ID', 'PROGRAM', 'MACHINE'], keep='first', inplace=True)


# In[118]:


print(tele_dup)


# In[119]:


missing_values = ["n/a", "na", "--"]


# In[120]:


tele.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




