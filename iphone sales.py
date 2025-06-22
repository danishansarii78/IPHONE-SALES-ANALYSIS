#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# In[ ]:





# In[5]:


data = pd.read_csv(r"C:\Users\DELL\Downloads\apple_products (1).csv")
print(data.head())


# In[6]:


#line to check whether this contains any null values
print(data.isnull().sum())


# In[7]:


print(data.describe())


# In[8]:


highest_rated=data.sort_values(by=["Star Rating"],ascending=False)
highest_rated=highest_rated.head(10)
print(highest_rated['Product Name'])


# In[10]:


iphones=highest_rated["Product Name"].value_counts()
label=iphones.index
counts=highest_rated["Number Of Ratings"]
figure=px.bar(highest_rated,x=label,y=counts,title="Number of Ratings of highest Rating iphones")
figure.show()


# In[14]:


# Group by Product Name and sum the number of ratings
grouped = highest_rated.groupby("Product Name")["Number Of Ratings"].sum().reset_index()

# Plot the grouped data
fig = px.bar(grouped, x="Product Name", y="Number Of Ratings",
             title="Number of Ratings for Highest Rated iPhones")

fig.show()


# In[12]:


figure=px.scatter(data_frame=data,x="Number Of Ratings",y="Sale Price",size="Discount Percentage",trendline="ols",title="Relationship between sales price and number of rating")
figure.show()


# In[13]:


figure=px.scatter(data_frame=data,x="Number Of Ratings",y="Discount Percentage",size="Sale Price",trendline="ols",title="Relationship between discount and number of ratings")
figure.show()


# In[ ]:


####summmary####
#####apple iphone 8 plus was the most appreciated iphones in Indida

