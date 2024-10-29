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
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import geodatasets

# %%
df = pd.read_csv('earthquakes.csv')
df.set_index('ID', inplace=True)

df.Type.unique()

# %%
df.head(10)

# %%
df2=df[df.Type != 'Earthquake']

def pictogramme(df2):
    world = gpd.read_file(geodatasets.get_path("naturalearth.land"))
    world.plot(color='white', edgecolor='black')

    plt.scatter(df[(df.Type=="Nuclear Explosion")].Longitude, df[(df.Type=="Nuclear Explosion")].Latitude, marker="^")
    plt.scatter(df[(df.Type=="Explosion")].Longitude, df[(df.Type=="Explosion")].Latitude, marker="*", color="r")
    plt.scatter(df[(df.Type=="Rock Burst")].Longitude, df[(df.Type=="Rock Burst")].Latitude, marker="d", color="g")
    plt.xlim(-180, 180)
    plt.ylim(-90, 90)
    plt.show()


# %%
pictogramme(df2)

# %%
