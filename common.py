# Ceci est le fichier commun avec nos fonctions

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import geodatasets
import numpy as np
import matplotlib.pylab as pylab
from shapely.geometry import Point
from scipy import ndimage
from PIL import Image

df = pd.read_csv('earthquakes.csv')
df.set_index('ID', inplace=True)


def suppression_donnees(df):
    '''prend en argument une dataframe df contenant les données des tremblements de terre
    renvoie une dataframe avec la date, l'heure, la localisation, la profondeur et la magnitude'''
    df.drop(['Depth Error', 'Depth Seismic Stations', 'Magnitude Type', 'Magnitude Error', 'Magnitude Seismic Stations'], axis=1, inplace=True)
    df.drop(['Azimuthal Gap', 'Horizontal Distance', 'Horizontal Error', 'Root Mean Square'], axis=1, inplace=True) 
    df.drop(['Source', 'Location Source', 'Status', 'Magnitude Source'], axis=1, inplace=True)
    return df[df.Type == 'Earthquake']


df_propre = suppression_donnees(df)


def map(longitude, latitude):
    """carte des tremblements de terre"""
    world = gpd.read_file(geodatasets.get_path('naturalearth.land'))
    world.plot(color='white', edgecolor='black')
    plt.scatter(longitude, latitude, s=0.1, color='r')
    plt.xlim(-180,180)
    plt.ylim(-90,90)
    plt.show()


map(df_propre.Longitude, df_propre.Latitude)


def magnitude(df):
    world = gpd.read_file(geodatasets.get_path("naturalearth.land"))
    world.plot(color='white', edgecolor='black')
    plt.scatter(df[(df.Magnitude < 6) & (df.Magnitude >=5)].Longitude, df[(df.Magnitude < 6) & (df.Magnitude >=5)].Latitude, s=0.5, color='b', alpha=0.5)
    plt.scatter(df[(df.Magnitude < 7) & (df.Magnitude >=6)].Longitude, df[(df.Magnitude < 7) & (df.Magnitude >=6)].Latitude, s=1, color='g', alpha=0.5)
    plt.scatter(df[(df.Magnitude < 8) & (df.Magnitude >=7)].Longitude, df[(df.Magnitude < 8) & (df.Magnitude >=7)].Latitude, s=2.5, color='orange', alpha=0.5)
    plt.scatter(df[(df.Magnitude < 10) & (df.Magnitude >=8)].Longitude, df[(df.Magnitude < 10) & (df.Magnitude >=8)].Latitude, s=5, color='red', alpha=0.5)
    plt.xlim(-180, 180)
    plt.ylim(-90, 90)
    plt.show()


magnitude(df_propre)


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


zoom_japon(df)
