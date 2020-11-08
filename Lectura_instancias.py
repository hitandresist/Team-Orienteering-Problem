import networkx as nx
import matplotlib.pyplot as plt
import itertools as itools
import pandas as pd
import numpy as np
import scipy.spatial as sc

class Instancia_TOP():
    """En este objeto se guardan los datos necesarios para
    instanciar el Orienteering Problem. Los lee desde un
     fichero txt con un formato determinado.

     El origen de los mismos los pueden encontrar en
     https://www.mech.kuleuven.be/en/cib/op, así como una
     explicación detallada del significado de cada uno de
     los valores"""

    def __init__(self, filepath):
        
        self.filepath = filepath
        
        def read_data_instance(path):
            
            POIs = pd.read_csv(path, 
                               sep="\t", 
                               header = None , 
                               names=("coor_x","coor_y", "profit") , 
                               skiprows=(0,1,2))
            
            constraints = pd.read_csv(path,
                                      sep=" ", 
                                      header = None, 
                                      nrows=3)

            tmax = constraints.iloc[2,1]
            n = constraints.iloc[0,1]
            m = constraints.iloc[1,1]
            
            nodes = np.arange(0, n),
            coor_x = np.array(POIs.iloc[:,0])
            coor_y = np.array(POIs.iloc[:,1])
            profit = np.array(POIs.iloc[:,2])
            coor = np.array([coor_x, coor_y]).T
            
            edges = np.sqrt(np.sum((coor[None, :] - coor[:, None])**2, -1))
            
       
            return [tmax, n, m, nodes, coor_x, coor_y, coor, profit, edges]
        
        self.instance_data = read_data_instance(self.filepath)
        self.B_time_budget = self.instance_data[0]
        self.N_nodes       = self.instance_data[1]
        self.k_routes      = self.instance_data[2]
        self.nodes         = self.instance_data[3]
        self.coor_x        = self.instance_data[4]
        self.coor_y        = self.instance_data[5]
        self.coor          = self.instance_data[6]
        self.profit        = self.instance_data[7]
        
        
        self.edges         = self.instance_data[8]
        
    def get_data(self, mode = "dict"):
        
        if mode == "list":
            return self.instance_data
        
        if mode == "dict":
            return {
                "tmax"     : self.B_time_budget, 
                "N_nodes"  : self.N_nodes,
                "k_routes" : self.k_routes,
                "nodes"    : self.nodes,
                "coor_x"   : self.coor_x,
                "coor_y"   : self.coor_y,
                "profit"   : self.profit
                }
        
        


TOP_Instance_1 = Instancia_TOP("C:/Users/Andres Prieto/Documents/Master Investigación en Inteligencia Artificial/Resolución de Problemas con Metaheurísticos/Trabajo/Team_Orienteering_Problem/TOP_Inst/Set_21_234/p2.2.a.txt")
        
print(TOP_Instance_1.get_data())
print(TOP_Instance_1.get_data(mode="list"))

tmax, n, m, nodes, coor_x, coor_y, coor, profit, edges = TOP_Instance_1.get_data(mode="list")


