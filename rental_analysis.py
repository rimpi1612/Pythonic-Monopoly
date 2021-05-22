#!/usr/bin/env python
# coding: utf-8

# In[2]:


import panel as pn
pn.extension('plotly')
import plotly.express as px
import pandas as pd
import hvplot.pandas
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
from dotenv import load_dotenv

import warnings
warnings.filterwarnings('ignore')


# In[91]:


#MAPBOX_TOKEN 
load_dotenv()
mapbox_token = os.getenv("MAPBOX_TOKEN")


# In[92]:


#load csv and set year as index
sfo_data = pd.read_csv("Data/sfo_neighborhoods_census_data.csv", index_col="year")
sfo_data.head()


# In[93]:


# Calculate the mean number of housing units per year # class note 4.2
housing_units = sfo_data.groupby(['year'])['housing_units']
housing_units_mean = housing_units.mean()
housing_units_min = housing_units_mean.min()
housing_units_max = housing_units_mean.max()
housing_units_std = housing_units_mean.std()
housing_units_mean


# In[47]:


housing_units_min


# In[48]:


housing_units_max


# In[49]:


housing_units_std


# In[23]:


# Save the dataframe as a csv file
housing_units_mean.to_csv("housing_units_mean.csv", index=False)


# In[53]:


# Use the Pandas plot function to plot the average housing units per year.
housing_units_mean.plot.bar(figsize=(8,8), x='Year', y='Housing Units',title='Housing Units in San-Francisco from 2010 to 2016')


# In[58]:


housing_units_mean.plot.bar(figsize=(8,8), x='Year', y='Housing Units',title='Housing Units in San-Francisco from 2010 to 2016')
#google
plt.ylim([housing_units_min-housing_units_std,housing_units_max+housing_units_std])


# In[59]:


# Calculate the average sale price per square foot and average gross rent
sfo_avg_price_rent_df = sfo_data[['sale_price_sqr_foot','gross_rent']].groupby(['year'])['sale_price_sqr_foot','gross_rent'].mean()
sfo_avg_price_rent_df


# In[96]:


# Create two line charts, one to plot the average sale price per square foot and another for average montly rent

# Line chart for average sale price per square foot
#reset index to make the year as x 
price_plot = sfo_avg_price_rent_df.reset_index().plot(
    x='year', 
    y='sale_price_sqr_foot', 
    title='Average Price per SqFt by Year',
    color='purple')
price_plot.set_ylabel("Price per SqFt")

# Line chart for average montly rent

gross_plot = sfo_avg_price_rent_df.reset_index().plot(
    x='year', 
    y='gross_rent', 
    title='Average Gross Rent by Year',
    color='red'
)
gross_plot.set_ylabel("Gross Rent")


# In[63]:


# Group by year and neighborhood and then create a new dataframe of the mean values
sfo_avg_price_by_neighborhood = sfo_data.groupby(['year','neighborhood']).mean().reset_index()
sfo_avg_price_by_neighborhood.head(10)


# In[65]:


# Use hvplot to create an interactive line chart of the average monthly rent. # class note 6.1
sfo_avg_price_by_neighborhood.hvplot.line(
    "year",
    "sale_price_sqr_foot",
    xlabel= "Year",
    ylabel="Avg. Sale Price per Square Foot",
    groupby="neighborhood",
)


# In[67]:


# Use hvplot to create an interactive line chart of the average monthly rent.
sfo_avg_price_by_neighborhood.hvplot.line(
    "year",
    "gross_rent",
    xlabel= "Year",
    ylabel="Avg. Gross Rent",
    groupby="neighborhood",
)


# In[70]:


# Getting the data from the top 10 expensive neighborhoods to own
top10_neighborhoods = sfo_data.groupby(['neighborhood']).mean()
top10_neighborhoods.sort_values(['sale_price_sqr_foot'], ascending=False, inplace=True)
top10_neighborhoods = top10_neighborhoods.reset_index().head(10)
top10_neighborhoods


# In[115]:


# Plotting the data from the top 10 expensive neighborhoods
top10_neighborhoods.hvplot.bar(
    "neighborhood",
    "sale_price_sqr_foot",
    title="Top 10 Expensive Neighborhoods in SFO",
    xlabel="Neighborhood",
    ylabel="Avg. Sale Price per Square Foot",
    height=500,
    rot=90
).opts(yformatter="%.0f")


# In[ ]:





# In[72]:


# Fetch the previously generated DataFrame that was grouped by year and neighborhood
sfo_avg_price_by_neighborhood.head(10)


# In[79]:


sfo_avg_price_by_neighborhood.hvplot.bar(
    x='year', 
    y=['sale_price_sqr_foot', 'gross_rent'], 
    xlabel='Year', 
    ylabel='Avg price, Gross rent', 
    groupby='neighborhood', 
    rot=90, 
    width=700, 
    height=500
).opts(yformatter="%.0f")


# In[80]:


# Load neighborhoods coordinates data
coordinates_df = pd.read_csv("Data/neighborhoods_coordinates.csv")
coordinates_df.head()


# In[86]:


# Calculate the mean values for each neighborhood
neighborhood_mean_df = sfo_data.groupby(['neighborhood']).mean().reset_index()
neighborhood_mean_df.head()


# In[90]:


# Join the average values with the neighborhood locations # class note 4.2
combined_df = pd.concat([neighborhood_mean_df, coordinates_df], axis='columns', join='inner')
combined_df = combined_df.dropna()
combined_df.drop(columns=['Neighborhood'], inplace=True)
combined_df.head()


# In[97]:


# Set the mapbox access token
px.set_mapbox_access_token(mapbox_token)


# In[191]:


# Create a scatter mapbox to analyze neighborhood info
# stackoverflow helped for color change
map_plot = px.scatter_mapbox(
    combined_df,
    lat="Lat",
    lon="Lon",
    size="sale_price_sqr_foot",
    color="gross_rent",
    color_continuous_scale=px.colors.cyclical.IceFire,
    hover_name="neighborhood",
    title="Averange Sale Price Per Square Foot and Gross Rent in San Francisco",
    zoom=11
)
map_plot.show()


# In[ ]:





# In[168]:


# Fetch the data from all expensive neighborhoods per year.
df_expensive_neighborhoods_per_year = sfo_avg_price_by_neighborhood[sfo_avg_price_by_neighborhood["neighborhood"].isin(top10_neighborhoods["neighborhood"])]
df_expensive_neighborhoods_per_year.head(10)


# In[189]:


plot = px.parallel_categories(
    top10_neighborhoods,
    dimensions=['neighborhood', 'sale_price_sqr_foot', 'housing_units', 'gross_rent'],
    color='sale_price_sqr_foot',
    color_continuous_scale=px.colors.sequential.Inferno,
    labels={
        'neighborhood': 'neighborhood',
        'sale_price_sqr_foot': 'sale_price_sqr_foot',
        'housing_units': 'housing_units',
        'gross_rent': 'gross_rent'
    },
    width=1000,
)
plot.show()


# In[ ]:





# In[190]:


# Parallel Categories Plot
px.parallel_coordinates(
    top10_neighborhoods, 
    color='sale_price_sqr_foot',
    title = 'Parallel Coordinates Plot of Most Expensive Neighborhoods in San Francisco per Year'
)


# In[175]:


px.sunburst(
    df_expensive_neighborhoods_per_year, 
    path=['year','neighborhood'], 
    color='gross_rent', 
    color_continuous_scale='RdBu',
    title = 'Costs Analysis of Most Expensive Neighborhoods in San Francisco per Year'
)


# In[ ]:





# In[ ]:





# In[ ]:




