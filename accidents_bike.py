# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 10:58:12 2016

@author: babou
"""

import pandas as pd
import numpy as np

accidents = pd.read_csv('data/accidents-corporels-de-la-circulation-en-france.csv', sep=";",
                        dtype={"Code Insee" : np.dtype('str')})


# Il n'éxiste pas de données sur le nombre d'accident sur les vélos en France.
# Nous prennons donc l'hypothèse que si l'accident se déroule sur une piste cyclable,
# un vélo y est impliqué.

# Uniquement accident sur piste cyclable / bande cyclable
bike = accidents[accidents["Voie spéciale"].str.contains("cyclable", na=False)]

# On regroupe le nombre d'accident par ville
grp_insee = bike.groupby(['Code Insee']).size().reset_index()
grp_insee.columns = ['COM', 'accident_velo']

# export
grp_insee.to_csv('data/accident_bike_com.csv', index=False)
