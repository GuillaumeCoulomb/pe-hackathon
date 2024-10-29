# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import geopandas as gpd
import geodatasets
import pandas as pd
import matplotlib.pyplot as plt

# %%
df = pd.read_csv("earthquakes.csv", index_col='ID')

# %%

# %%
plt.scatter(df.Longitude, df.Latitude, s=4, color='r')
plt.xlim(-180,180)
plt.ylim(-90,90)

# %%
#il faut tout d'abord pip install geodatasets
#geodatasets.data
world = gpd.read_file(geodatasets.get_path('naturalearth.land'))

# %%
#on superpose la map monde avec nos tremblements de terre
world.plot(color='white', edgecolor='black')
plt.scatter(df.Longitude, df.Latitude, s=0.1, color='r')
plt.xlim(-180,180)
plt.ylim(-90,90)
plt.show()


# %%

# %%
def map(longitude, latitude):
    world = gpd.read_file(geodatasets.get_path('naturalearth.land'))
    

# %%
