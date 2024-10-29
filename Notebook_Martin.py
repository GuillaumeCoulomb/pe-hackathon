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
import pandas as pd
import matplotlib.pyplot as plt
import geodatasets

# %%
df = pd.read_csv('earthquakes.csv')
df.head(10)
df.set_index('ID', inplace=True)
df

# %%
world = gpd.read_file(geodatasets.get_path("naturalearth.land"))
world.plot(color='white', edgecolor='black')
plt.scatter(df.Longitude, df.Latitude, s=0.1, color='r')
plt.xlim(-180, 180)
plt.ylim(-90, 90)
plt.show()

# %%
world = gpd.read_file(geodatasets.get_path("naturalearth.land"))
world.plot(color='white', edgecolor='black')
plt.scatter(df[(df.Magnitude < 6) & (df.Magnitude >=5)].Longitude, df[(df.Magnitude < 6) & (df.Magnitude >=5)].Latitude, s=0.5, color='b')
plt.scatter(df[(df.Magnitude < 7) & (df.Magnitude >=6)].Longitude, df[(df.Magnitude < 7) & (df.Magnitude >=6)].Latitude, s=1, color='g')
plt.scatter(df[(df.Magnitude < 8) & (df.Magnitude >=7)].Longitude, df[(df.Magnitude < 8) & (df.Magnitude >=7)].Latitude, s=2.5, color='orange')
plt.scatter(df[(df.Magnitude < 10) & (df.Magnitude >=8)].Longitude, df[(df.Magnitude < 10) & (df.Magnitude >=8)].Latitude, s=5, color='red')
plt.xlim(-180, 180)
plt.ylim(-90, 90)
plt.show()
