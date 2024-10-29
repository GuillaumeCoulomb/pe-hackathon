# Ceci est le fichier commun avec nos fonctions

import pandas as pd

df = pd.read_csv('earthquakes.csv')


def suppression_donnees(df):
    '''prend en argument une dataframe df contenant les données des tremblements de terre
    renvoie une dataframe avec la date, l'heure, la localisation, la profondeur et la magnitude'''
    df.set_index('ID', inplace = True)
    df.drop(['Depth Error', 'Depth Seismic Stations', 'Magnitude Type', 'Magnitude Error', 'Magnitude Seismic Stations'], axis=1, inplace=True)
    df.drop(['Azimuthal Gap', 'Horizontal Distance', 'Horizontal Error', 'Root Mean Square'], axis=1, inplace=True) 
    df.drop(['Source', 'Location Source', 'Status', 'Magnitude Source'], axis=1, inplace=True)
    return df[df.Type == 'Earthquake']


supression_donnees(df).head(5)



plt.scater
