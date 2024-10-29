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

# %%
df = pd.read_csv('earthquakes.csv')


# %%
def supression_donnees(df):
    '''prend en argument une dataframe df contenant les données des tremblements de terre
    renvoie une dataframe avec la date, l'heure, la localisation, la profondeur et la magnitude'''
    df.set_index('ID', inplace = True)
    df.drop(['Depth Error', 'Depth Seismic Stations', 'Magnitude Type', 'Magnitude Error', 'Magnitude Seismic Stations'], axis=1, inplace=True)
    df.drop(['Azimuthal Gap', 'Horizontal Distance', 'Horizontal Error', 'Root Mean Square'], axis=1, inplace=True) 
    df.drop(['Source', 'Location Source', 'Status', 'Magnitude Source'], axis=1, inplace=True)
    return df[df.Type == 'Earthquake']




# %%
df1 = pd.read_csv('earthquakes.csv')
df2 = supression_donnees(df1)

# %%
df2.head(20)

# %%
df2.Type.unique()

# %%

# %%

# %%
