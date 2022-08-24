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

# In[6]:


import pandas as pd
import numpy as np
from IPython.display import Image


# In[7]:


tele=pd.read_csv(r"C:\Users\Genet Shanko\Desktop\Week_1_challange\Week1_challenge_data_source(CSV).csv",na_values=['numeric_only',None])
tele.head()


# The above telocm data have 5 rows with 55 column. the follwoing data shows the number of column avialbe in the dataset

# In[8]:


tele.columns.tolist()


# to have general information about the dat frame

# In[9]:


tele.info()


# In[10]:


len(tele.columns)


# In[11]:


totalcells= len(tele)
totalcells


# To exploer the types and number of data points, the follwoing code may support

# In[12]:


tele.shape


# In[13]:


print(f" There are {tele.shape[0]} rows and {tele.shape[1]} columns")


# To identifay the null value within the dataset 

# In[14]:


tele.isnull()


# To explor the number of the null value in each column and totol null value as a whole 

# In[15]:


tele.isnull().sum()


# In[16]:


tele.isnull().sum().sum()


# ##### Handling missing values 

# Before handling the missing value , let us check the data distrbusion 

# In[17]:


missingCount = tele.isnull().sum()
missingCount


# In[18]:


totalMissing = missingCount.sum()
totalMissing


# In[19]:


totalCells = np.product(tele.shape)
totalCells 


# In[20]:



print("The Telecome dataset contains", round(((totalMissing/totalcells)*100), 2), "%", "missing values.")


# In[21]:


tele.isna().sum()


# In[22]:


tele.skew(axis=0)


# In[23]:


To veiw the data types of each of the 


# In[24]:


tele.dtypes


# In[25]:


import seaborn as sns
sns.displot(data=tele, x=tele['Handset Manufacturer'])


# the following figure shows the number of handset manfacturer  and the number appratus used by custmers

# In[26]:


tele['Handset Manufacturer'].hist()


# In[27]:


tele['Handset Type'].hist()


# to have the gneral discription of the dataset 

# In[ ]:





# In[ ]:





# Drope single value column

# In[32]:


tele_data=tele.copy()
single_value_columns = pd.DataFrame(tele_data.apply(lambda x: len(x.value_counts()), axis=0), columns=['SingleValueColumn'])
drop_single_value_columns = list(single_value_columns.loc[single_value_columns['SingleValueColumn']==1].index)
print('Columns which have just a single value => \n\n' + str(drop_single_value_columns))
tele.drop(drop_single_value_columns, axis=1, inplace=True)
print('\n\nRemaining Columns => ' + str(len(tele.columns)))


# to count  duplicated column use 

# In[33]:


# Count of duplicates
tele.duplicated().value_counts()
# Drop duplicates
tele_dup=tele.drop_duplicates(keep='first', inplace=True)
#tele.drop_duplicates(subset=['custem_ID', 'PROGRAM', 'MACHINE'], keep='first', inplace=True)


# In[34]:


print(tele_dup)


# In[35]:


missing_values = ["n/a", "na", "--"]


# In[36]:


tele.head()


#  how to drope a row 

# In[37]:


# Drop rows containing all missing values
 
# drop columns with more than 30% missing values
tele_clean = tele.drop(['Start ms', 'End ms', 'Start', 'End','DL TP < 50 Kbps (%)','250 Kbps < DL TP < 1 Mbps (%)',
                        'DL TP > 1 Mbps (%)','UL TP < 10 Kbps (%)','UL TP < 10 Kbps (%)','10 Kbps < UL TP < 50 Kbps (%)','UL TP > 300 Kbps (%)'], axis=1)
tele_clean.shape


# for filling the missing value

# In[ ]:


def fix_missing_ffill(tele_clean, col):
    tele_clean[col] = tele_clean[col].fillna(method='ffill')
    return tele_clean[col]


def fix_missing_bfill(tele_clean, col):
    tele_clean[col] = tele_clean[col].fillna(method='bfill')
    return tele_clean[col]

tele_clean['diag_1'] = fix_missing_ffill(tele_clean, 'diag_1')
tele_clean['diag_2'] = fix_missing_ffill(tele_clean, 'diag_2')
tele_clean['diag_3'] = fix_missing_ffill(tele_clean, 'diag_3')

# fill 'race' column with mode 
#tele_clean['race'] = df_clean['race'].fillna(df_clean['race'].mode()[0])


# In[41]:


from sklearn.preprocessing import MinMaxScaler

minmax_scaler = MinMaxScaler()

# generate 1000 data points randomly drawn from an exponential distribution
tele = pd.DataFrame(np.random.exponential(200, size=2000))

tele.sample(5)


# In[43]:


tele[0].min(), tele[0].max()


# In[47]:


# mix-max scale the data between 0 and 1
import matplotlib.pyplot as plt
def scaler(tele):
    scaled_data = minmax_scaler.fit_transform(tele)

    # plot both together to compare
    fig, ax = plt.subplots(1,2, figsize=(10, 6))
    sns.histplot(tele, ax=ax[0])
    ax[0].set_title("Original Data")
    sns.histplot(scaled_data, ax=ax[1])
    ax[1].set_title("Scaled data")
    
scaler(tele)


# Normal sdistrbutions

# In[48]:


from sklearn.preprocessing import Normalizer

def normalizer(tele):
    norm = Normalizer()
    # normalize the exponential data with boxcox
    normalized_data = norm.fit_transform(tele)

    # plot both together to compare
    fig, ax=plt.subplots(1,2, figsize=(10, 6))
    sns.histplot(tele, ax=ax[0])
    ax[0].set_title("Original Data")
    sns.histplot(normalized_data[0], ax=ax[1])
    ax[1].set_title("Normalized data")

normalizer(tele)


# In[49]:


# check datatypes
tele_clean.info()


# It continue 

# In[ ]:




