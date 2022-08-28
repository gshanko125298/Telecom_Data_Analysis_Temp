#!/usr/bin/env python
# coding: utf-8
Sessions frequency
Duration of the session
Sessions total traffic (download and upload (bytes))
# In[1]:


#import python library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import math
import seaborn as sns
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go  
from IPython.display import Image
from sklearn import preprocessing
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
from sklearn.preprocessing import StandardScaler, normalize


# In[2]:


df_tele=pd.read_csv(r"C:\Users\Genet Shanko\Desktop\Week_1_challange\Week1_challenge_data_source(CSV).csv",na_values=['?',"n.a.","NA","n/a", "na", None])
df_tele.head()


# In[3]:


df_tele.columns.tolist()


# In[4]:


# check datatypes
df_tele.info()


# In[5]:


print(f" There are {df_tele.shape[0]} rows and {df_tele.shape[1]} columns")


# In[6]:


users_data = df_tele.groupby('MSISDN/Number')


# In[7]:


users_sessions= users_data['Bearer Id'].count()
users_sessions.head(10)


# In[8]:


users_sessions= users_data['Dur. (ms)'].sum()
users_sessions


# In[9]:


# Aggregation of Total values
df_tele["Total Uploads"]=df_tele["Google UL (Bytes)"]+df_tele["Email UL (Bytes)"]+df_tele["Social Media UL (Bytes)"]+df_tele["Youtube UL (Bytes)"]+df_tele["Netflix UL (Bytes)"]+df_tele["Gaming UL (Bytes)"]+df_tele["Other UL (Bytes)"]
df_tele["Total Downloads"]=df_tele["Google DL (Bytes)"]+df_tele["Email DL (Bytes)"]+df_tele["Social Media DL (Bytes)"]+df_tele["Youtube DL (Bytes)"]+df_tele["Netflix DL (Bytes)"]+df_tele["Gaming DL (Bytes)"]+df_tele["Other DL (Bytes)"]
df_tele['Total UL and DL']=df_tele['Total DL (Bytes)']+df_tele["Total UL (Bytes)"]# Aggregation of Total Social Media data


# In[10]:


df_tele["Youtube_Total_Data"]=df_tele["Youtube DL (Bytes)"]+df_tele["Youtube UL (Bytes)"]
df_tele["Google_Total_Data"]=df_tele["Google DL (Bytes)"]+df_tele["Google UL (Bytes)"]
df_tele["Email_Total_Data"]=df_tele["Email DL (Bytes)"]+df_tele["Email UL (Bytes)"]
df_tele["Social_Media_Total_Data"]=df_tele["Social Media DL (Bytes)"]+df_tele["Social Media UL (Bytes)"]
df_tele["Netflix_Total_Data"]=df_tele["Netflix DL (Bytes)"]+df_tele["Netflix UL (Bytes)"]
df_tele["Gaming_Total_Data"]=df_tele["Gaming DL (Bytes)"]+df_tele["Gaming UL (Bytes)"]
df_tele["Other_Total_Data"]=df_tele["Other DL (Bytes)"]+df_tele["Other UL (Bytes)"]


# In[11]:


Tele_users = df_tele[['MSISDN/Number', 'Bearer Id', 'Dur. (ms).1', 'Total UL and DL']].copy().rename(columns={'Dur. (ms).1': 'time_duration'})
Tele_users


# In[12]:


Tele_users = Tele_users.groupby('MSISDN/Number').agg({'Bearer Id': 'count', 'time_duration': 'sum', 'Total UL and DL': 'sum'})
Tele_users = Tele_users.rename(columns={'Bearer Id': 'sessions'})
Tele_users.head(10)


# In[13]:


Tele_users.nlargest(10, 'time_duration')


# In[14]:


Tele_users.nlargest(10, 'time_duration')


# In[15]:


import plotly.io as pio
from IPython.display import Image
def mult_hist(sr, rows, cols, title_text, subplot_titles, interactive=False):
    fig = make_subplots(rows=rows, cols=cols, subplot_titles=subplot_titles)
    for i in range(rows):
        for j in range(cols):
            x = ["-> " + str(i) for i in sr[i+j].index]
            fig.add_trace(go.Bar(x=x, y=sr[i+j].values), row=i+1, col=j+1)
    fig.update_layout(showlegend=False, title_text=title_text)
    if(interactive):
        fig.show()
    else:
        return Image(pio.to_image(fig, format='png', width=1200))


# In[35]:


from plotly.subplots import make_subplots
import plotly.graph_objects as go

sessions = Tele_users.nlargest(10, "sessions")['sessions']
duration =Tele_users.nlargest(10, "time_duration")['time_duration']
data_volume = Tele_users.nlargest(10, "Total UL and DL")['Total UL and DL']

mult_hist([sessions, duration, data_volume], 1,3, "User metrix", ['sessions', 'time_duration','Total UL and DL'])


# In[17]:


Tele_users.boxplot()


# In[18]:


scaler = StandardScaler()
scaled_array = scaler.fit_transform(Tele_users)
pd.DataFrame(scaled_array).head(5)


# In[19]:


data_normalized = normalize(scaled_array)
pd.DataFrame(data_normalized).head(5)


# In[20]:


kmeans = KMeans(n_clusters=3, random_state=0).fit(data_normalized)
kmeans.labels_


# In[ ]:





# In[24]:


Tele_users.insert(0, 'Cluster', kmeans.labels_)
Tele_users.head(5)


# In[25]:


fig = px.scatter(Tele_users, x='Total UL and DL', y="time_duration", color='Cluster', size='sessions')
Image(pio.to_image(fig, format='png', width=1200))


# In[27]:


cluster_user = Tele_users[Tele_users["Cluster"]==0]
cluster_user.describe()


# In[28]:


cluster_user = Tele_users[Tele_users["Cluster"]==1]
cluster_user.describe()


# In[29]:


cluster1 = Tele_users[Tele_users["Cluster"]==2]
cluster1.describe()


# In[31]:


apps_df_tele = df_tele.groupby('MSISDN/Number').agg({'Gaming_Total_Data': 'sum', 'Youtube_Total_Data': 'sum', 'Netflix_Total_Data': 'sum',                     'Google_Total_Data': 'sum', 'Email_Total_Data': 'sum', 'Social_Media_Total_Data': 'sum', 'Other_Total_Data': 'sum'})
apps_df_tele.head(10)


# In[33]:


from plotly.subplots import make_subplots
import plotly.graph_objects as go
Gaming_Data = apps_df_tele.nlargest(10, "Gaming_Total_Data")['Gaming_Total_Data']
Youtube_Data = apps_df_tele.nlargest(10, "Youtube_Total_Data")['Youtube_Total_Data']
Netflix_Data = apps_df_tele.nlargest(10, "Netflix_Total_Data")['Netflix_Total_Data']
Google_Data = apps_df_tele.nlargest(10, "Google_Total_Data")['Google_Total_Data']
Email_Data = apps_df_tele.nlargest(10, "Email_Total_Data")['Email_Total_Data']
Social_Media = apps_df_tele.nlargest(10, "Social_Media_Total_Data")['Social_Media_Total_Data']
Other_Data = apps_df_tele.nlargest(10, "Other_Total_Data")['Other_Total_Data']


mult_hist([Gaming_Data, Youtube_Data, Netflix_Data], 1,
          3, "User metrix", ["Gaming_Data", "Youtube_Data", "Netflix_Data"])


# In[36]:


mult_hist([Google_Data, Email_Data, Social_Media, Other_Data], 1,
          4, "User metrix", [ "Google_Data", "Email_Data", "Social Media", "Other_Data"])

...........................