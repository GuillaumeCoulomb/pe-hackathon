# Ceci est le fichier commun avec nos fonctions

import pandas as pd

df = pd.read_csv('earthquakes.csv')


def supression_donnees(df):
    '''prend en argument une dataframe df contenant les données des tremblements de terre
    modiie la dataframe pour avoir la date, l'heure, la localisation, la profondeur et la magnitude'''
    df.set_index('ID', inplace = True)
    df.drop(['Depth Error', 'Depth Seismic Stations', 'Magnitude Type', 'Magnitude Error', 'Magnitude Seismic Stations'], axis=1, inplace=True)
    df.drop(['Azimuthal Gap', 'Horizontal Distance', 'Horizontal Error', 'Root Mean Square'], axis=1, inplace=True) 
    df.drop(['Source', 'Location Source', 'Status', 'Magnitude Source', 'Type'], axis=1, inplace=True)


supression_donnees(df)




