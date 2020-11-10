# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 22:55:13 2020

@author: Andres Prieto
"""

from Lectura_instancias import *

TOP_Inst = Instancia_TOP("C:/Users/Andres Prieto/Documents/Master Investigación en Inteligencia Artificial/Resolución de Problemas con Metaheurísticos/Trabajo/Team_Orienteering_Problem/TOP_Inst/Set_21_234/p2.2.a.txt")


edges = list(itools.combinations(self.nodes, 2))
        

        
nodes_out = [(i , self.distances[ 0 , i] + self.distances[i, self.N_nodes - 1]) for i in nodes if self.distances[ 0 , i] + self.distances[i, self.N_nodes - 1] > self.B_time_budget]
            
        
G = nx.Graph()
G.add_nodes_from(nodes)
#G.add_edges_from(edges)
        
color_node = []
position = { i : (coor_x[i], coor_y[i]) for i in nodes}

plt.plot(1)
nx.draw_networkx(G, pos = position , with_labels=True , node_size=self.profit*10)
plt.show()