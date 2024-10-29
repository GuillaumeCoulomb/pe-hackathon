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
import numpy as np
import matplotlib.pylab as pylab
from shapely.geometry import Point
from scipy import ndimage
from PIL import Image

# %%
df = pd.read_csv('earthquakes.csv')

# %%
df.head(5)


# %%
def suppression_donnees(df):
    '''prend en argument une dataframe df contenant les données des tremblements de terre
    renvoie une dataframe avec la date, l'heure, la localisation, la profondeur et la magnitude'''
    df.set_index('ID', inplace = True)
    df.drop(['Depth Error', 'Depth Seismic Stations', 'Magnitude Type', 'Magnitude Error', 'Magnitude Seismic Stations'], axis=1, inplace=True)
    df.drop(['Azimuthal Gap', 'Horizontal Distance', 'Horizontal Error', 'Root Mean Square'], axis=1, inplace=True) 
    df.drop(['Source', 'Location Source', 'Status', 'Magnitude Source'], axis=1, inplace=True)
    return df[df.Type == 'Earthquake']




# %%
df1 = pd.read_csv('earthquakes.csv')
df2 = suppression_donnees(df1)

# %%
df2.head(20)

# %%
df2.Type.unique()


# %%
# X = df.Date
# Y = df.Magnitude
# plt.scatter(X, Y, color='r', s=0.5)
# plt.show()

# %%

# %%
def magnitude(df):
    world = gpd.read_file(geodatasets.get_path("naturalearth.land"))
    world.plot(color='white', edgecolor='black')
    plt.scatter(df[(df.Magnitude < 6) & (df.Magnitude >=5)].Longitude, df[(df.Magnitude < 6) & (df.Magnitude >=5)].Latitude, s=0.5, color='b')
    plt.scatter(df[(df.Magnitude < 7) & (df.Magnitude >=6)].Longitude, df[(df.Magnitude < 7) & (df.Magnitude >=6)].Latitude, s=1, color='g')
    plt.scatter(df[(df.Magnitude < 8) & (df.Magnitude >=7)].Longitude, df[(df.Magnitude < 8) & (df.Magnitude >=7)].Latitude, s=2.5, color='orange')
    plt.scatter(df[(df.Magnitude < 10) & (df.Magnitude >=8)].Longitude, df[(df.Magnitude < 10) & (df.Magnitude >=8)].Latitude, s=5, color='red')
    plt.xlim(-180, 180)
    plt.ylim(-90, 90)
    plt.show()


# %%

# %%
# df2['Year'] = df2['Date'].map(lambda x: x.years)
# df2['year'] = pd.DatetimeIndex(df2['Date']).year

# %%
df2.head(5)


# %%
def zoom_japon(df):
    world = gpd.read_file(geodatasets.get_path("naturalearth.land"))
    world.plot(color='white', edgecolor='black')
    plt.scatter(df[(df.Magnitude < 6) & (df.Magnitude >=5)].Longitude, df[(df.Magnitude < 6) & (df.Magnitude >=5)].Latitude, s=0.5, color='b')
    plt.scatter(df[(df.Magnitude < 7) & (df.Magnitude >=6)].Longitude, df[(df.Magnitude < 7) & (df.Magnitude >=6)].Latitude, s=1, color='g')
    plt.scatter(df[(df.Magnitude < 8) & (df.Magnitude >=7)].Longitude, df[(df.Magnitude < 8) & (df.Magnitude >=7)].Latitude, s=2.5, color='orange')
    plt.scatter(df[(df.Magnitude < 10) & (df.Magnitude >=8)].Longitude, df[(df.Magnitude < 10) & (df.Magnitude >=8)].Latitude, s=5, color='red')
    plt.xlim(-180, 180)
    plt.ylim(-90, 90)
    plt.savefig("monde.png")
    im = Image.open("monde.png", "r")
    left = 450
    top = 120
    right = 575
    bottom = 250
    im2 = im.crop((left, top, right, bottom))
    im2.show()


# %%
def zoom_japon2(df):
    world = gpd.read_file(geodatasets.get_path("naturalearth.land"))
    world.plot(color='white', edgecolor='black')
    plt.scatter(df[(df.Magnitude < 6) & (df.Magnitude >=5)].Longitude, df[(df.Magnitude < 6) & (df.Magnitude >=5)].Latitude, s=0.5, color='b')
    plt.scatter(df[(df.Magnitude < 7) & (df.Magnitude >=6)].Longitude, df[(df.Magnitude < 7) & (df.Magnitude >=6)].Latitude, s=1, color='g')
    plt.scatter(df[(df.Magnitude < 8) & (df.Magnitude >=7)].Longitude, df[(df.Magnitude < 8) & (df.Magnitude >=7)].Latitude, s=2.5, color='orange')
    plt.scatter(df[(df.Magnitude < 10) & (df.Magnitude >=8)].Longitude, df[(df.Magnitude < 10) & (df.Magnitude >=8)].Latitude, s=5, color='red')
    plt.xlim(-180, 180)
    plt.ylim(-90, 90)
    plt.savefig("monde.png")
    im = Image.open("monde.png", "r")
    left = 450
    top = 120
    right = 575
    bottom = 250
    im2 = im.crop((left, top, right, bottom))
    im2.show()


# %%
zoom_japon2(df2):
    world = gpd.read_file(geodatasets.get_path("naturalearth.land"))
    world.plot(color='white', edgecolor='black')
    plt.scatter(df[(df.Magnitude < 6) & (df.Magnitude >=5)].Longitude, df[(df.Magnitude < 6) & (df.Magnitude >=5)].Latitude, s=0.5, color='b')
    plt.scatter(df[(df.Magnitude < 7) & (df.Magnitude >=6)].Longitude, df[(df.Magnitude < 7) & (df.Magnitude >=6)].Latitude, s=1, color='g')
    plt.scatter(df[(df.Magnitude < 8) & (df.Magnitude >=7)].Longitude, df[(df.Magnitude < 8) & (df.Magnitude >=7)].Latitude, s=2.5, color='orange')
    plt.scatter(df[(df.Magnitude < 10) & (df.Magnitude >=8)].Longitude, df[(df.Magnitude < 10) & (df.Magnitude >=8)].Latitude, s=5, color='red')
    plt.xlim(-180, 180)
    plt.ylim(-90, 90)
    plt.savefig("monde.png")
    im = Image.open("monde.png", "r")
    left = 450
    top = 120
    right = 575
    bottom = 250
    im2 = im.crop((left, top, right, bottom))
    im2.show()


# %%
def pictogramme(df2):
    world = gpd.read_file(geodatasets.get_path("naturalearth.land"))
    world.plot(color='white', edgecolor='black')
    plt.scatter(df[(df.Type=="Nuclear Explosion")].Longitude, df[(df.Type=="Nuclear Explosion")].Latitude, marker="^", label='Nuclear Explosion')
    plt.scatter(df[(df.Type=="Explosion")].Longitude, df[(df.Type=="Explosion")].Latitude, marker="*", color="r", label='Explosion')
    plt.scatter(df[(df.Type=="Rock Burst")].Longitude, df[(df.Type=="Rock Burst")].Latitude, marker="d", color="g", label='Rock Burst')
    plt.xlim(-180, 180)
    plt.ylim(-90, 90)
    plt.title('Sismique anthropocene')
    plt.legend()
    plt.show()



# %%
pictogramme(df2)

# %%
