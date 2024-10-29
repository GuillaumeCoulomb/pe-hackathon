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
from shapely.geometry import Point
import numpy as np

from scipy import ndimage

import matplotlib.pylab as pylab
import matplotlib.pyplot as plt


# %%
df = pd.read_csv("earthquakes.csv", index_col='ID')

# %%

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
    world.plot(color='white', edgecolor='black')
    plt.scatter(longitude, latitude, s=0.1, color='r')
    plt.xlim(-180,180)
    plt.ylim(-90,90)
    plt.show()


# %%
map(df.Longitude, df.Latitude)


# %%
def heatmap(d, bins=(100,100), smoothing=1.3, cmap='hot_r'):
    def getx(pt):
        return pt.coords[0][0]

    def gety(pt):
        return pt.coords[0][1]

    x = list(d.geometry.apply(getx))
    y = list(d.geometry.apply(gety))
    heatmap, xedges, yedges = np.histogram2d(y, x, bins=bins)
    extent = [yedges[0], yedges[-1], xedges[-1], xedges[0]]

    logheatmap = np.log(heatmap)
    logheatmap[np.isneginf(logheatmap)] = 0
    logheatmap = ndimage.filters.gaussian_filter(logheatmap, smoothing, mode='nearest')

    world = gpd.read_file(geodatasets.get_path('naturalearth.land'))
    world.plot(color='white', edgecolor='black')
    plt.imshow(logheatmap, cmap=cmap, extent=extent)
    plt.colorbar()
    plt.gca().invert_yaxis()
    plt.xlim(-180,180)
    plt.ylim(-90,90)
    plt.show()


# %%

# %%
pts = df[['Longitude', 'Latitude']]

# %%
pts['geometry'] = df.apply(lambda x: Point((float(x.Longitude), float(x.Latitude))), axis=1)

# %%
pts.head(2)

# %%
pts = gpd.GeoDataFrame(pts, geometry='geometry')

# %%
pts

# %%
heatmap(pts, bins=100, smoothing=1.5)


# %%
def frequence(pts):
    """prend en argument une dataframe, par exemple df[['Longitude', 'Latitude']]"""
    d = pts['geometry'] = df.apply(lambda x: Point((float(x.Longitude), float(x.Latitude))), axis=1)
    d = gpd.GeoDataFrame(pts, geometry='geometry')
    bins=100
    smoothing=1.5
    cmap= 'hot_r'
    
    def getx(pt):
        return pt.coords[0][0]

    def gety(pt):
        return pt.coords[0][1]

    x = list(d.geometry.apply(getx))
    y = list(d.geometry.apply(gety))
    heatmap, xedges, yedges = np.histogram2d(y, x, bins=bins)
    extent = [yedges[0], yedges[-1], xedges[-1], xedges[0]]

    logheatmap = np.log(heatmap)
    logheatmap[np.isneginf(logheatmap)] = 0
    logheatmap = ndimage.filters.gaussian_filter(logheatmap, smoothing, mode='nearest')

    world = gpd.read_file(geodatasets.get_path('naturalearth.land'))
    world.plot(color='white', edgecolor='black')
    plt.imshow(logheatmap, cmap=cmap, extent=extent)
    plt.colorbar()
    plt.gca().invert_yaxis()
    plt.show()


# %%
frequence(df[['Longitude', 'Latitude']])

# %%
