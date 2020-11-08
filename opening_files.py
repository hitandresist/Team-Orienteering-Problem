# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 22:55:13 2020

@author: Andres Prieto
"""

import pandas as pd
import numpy as np

POIs = pd.read_csv(
    "C:/Users/Andres Prieto/Documents/Master Investigación en Inteligencia Artificial/Resolución de Problemas con Metaheurísticos/Trabajo/Team_Orienteering_Problem/TOP_Inst/Set_21_234/p2.2.a.txt", 
    sep="\t", header = None , names=("coor_x","coor_y", "profit") , skiprows=(0,1,2))

print(POIs)

constraints = pd.read_csv("C:/Users/Andres Prieto/Documents/Master Investigación en Inteligencia Artificial/Resolución de Problemas con Metaheurísticos/Trabajo/Team_Orienteering_Problem/TOP_Inst/Set_21_234/p2.2.a.txt",
                          sep=" ", header = None, nrows=3)

print(constraints)

tmax = constraints.iloc[2,1]
n = constraints.iloc[0,1]
m = constraints.iloc[0,0]

print(type(tmax))


coor_x = POIs.iloc[:,0]
coor_y = POIs.iloc[:,1]
profit = POIs.iloc[:,2]

print(np.array(coor_x))

