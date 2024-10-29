# Ceci est le fichier commun avec nos fonctions

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import geodatasets

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


magnitude(df_propre)




