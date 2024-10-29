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
from geodatasets import get_path

# %%
data_brut = gpd.read_file('https://public.opendatasoft.com/explore/dataset/significant-earthquake-database/export/')

# %%
mode_emploi = gpd.read_file('https://public.opendatasoft.com/explore/dataset/significant-earthquake-database/information/')

# %%
