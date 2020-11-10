import networkx as nx
import matplotlib.pyplot as plt
import itertools as itools
import pandas as pd
import numpy as np
import scipy.spatial as sc
import operator

class TOP():
    """En este objeto se guardan los datos necesarios para
    instanciar el Orienteering Problem. Los lee desde un
     fichero txt con un formato determinado.

     El origen de los mismos los pueden encontrar en
     https://www.mech.kuleuven.be/en/cib/op, así como una
     explicación detallada del significado de cada uno de
     los valores"""

    def __init__(self, filepath = "C:/Users/Andres Prieto/Documents/Master Investigación en Inteligencia Artificial/Resolución de Problemas con Metaheurísticos/Trabajo/Team_Orienteering_Problem/TOP_Inst/Set_21_234/p2.2.a.txt"):
        
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
            n = int(constraints.iloc[0,1])
            m = int(constraints.iloc[1,1])
            
            nodes = np.arange(0, n)
            coor_x = np.array(POIs.iloc[:,0])
            coor_y = np.array(POIs.iloc[:,1])
            profit = np.array(POIs.iloc[:,2])
            coor = np.array([coor_x, coor_y]).T
            
            distances = np.sqrt(np.sum((coor[None, :] - coor[:, None])**2, -1))
            
       
            return tmax, n, m, nodes, coor_x, coor_y, coor, profit, distances
        
        self.instance_data = read_data_instance(self.filepath)
        self.B_time_budget = self.instance_data[0]
        self.N_nodes       = self.instance_data[1]
        self.k_routes      = self.instance_data[2]
        self.nodes         = self.instance_data[3]
        self.coor_x        = self.instance_data[4]
        self.coor_y        = self.instance_data[5]
        self.coor          = self.instance_data[6]
        self.profit        = self.instance_data[7]
        
        
        self.distances         = self.instance_data[8]
        
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
    def nodes_out_Tmax(self, node_0 = 0, nodes = None, Tmax = None):
        
        if nodes is None:
            nodes = self.nodes
        if Tmax is None:
            Tmax = self.B_time_budget
            
        nodes_out = [i for i in nodes if self.distances[ node_0 , i] + self.distances[i, self.N_nodes - 1] > Tmax]
        return nodes_out
    
    
    def valid_nodes(self, node_0 = 0, nodes = None, Tmax = None):
        
        if nodes is None:
            nodes = self.nodes
        if Tmax is None:
            Tmax = self.B_time_budget
            
        valid_nodes = [i for i in nodes if self.distances[ node_0 , i] + self.distances[i, self.N_nodes - 1] <= Tmax]
        return valid_nodes   
    
    def draw(self):
        
        n_in = self.valid_nodes()
        n_out = self.nodes_out_Tmax()
        
        edges = list(itools.combinations(self.nodes, 2))
        
        G = nx.Graph()
        G.add_nodes_from(self.nodes)
        #G.add_edges_from(edges)
        
        color = []
        
        for node in G:
            if (node == 0 or node == self.N_nodes - 1):
                color.append('green')
            elif node in n_in:
                color.append('blue')
            else:
                color.append('red')
                        
        position = { i : (self.coor_x[i], self.coor_y[i]) for i in self.nodes}

        plt.plot(1)
        nx.draw_networkx(G, pos = position , with_labels=True , node_size=self.profit**1.75, node_color = color )
        plt.show()
    
    def sorted_valid_nodes(self, node_0 = 0, nodes = None, Tmax = None):
        
        if nodes is None:
            nodes = self.nodes
        if Tmax is None:
            Tmax = self.B_time_budget
        
        # print(f"Nodo inicial: {node_0}"
        #       f"Lista de nodos: {nodes}"
        #       f"Tmax: {}")
        
        in_nodes = [[i, self.profit[i], self.distances[node_0, i]] for i in nodes if self.distances[node_0 , i] + self.distances[i, self.N_nodes - 1] <= Tmax ]
        
        in_nodes.sort(key = operator.itemgetter(1,2))
        
        return in_nodes        
        
    def inicialization(self):
        
        Ym = np.zeros((self.k_routes,1)).astype(int).tolist()
        SV_ini_nodes = self.sorted_valid_nodes()
        t_consumed = np.zeros((self.k_routes,1)).astype(int).tolist()
        SV_nodes = SV_ini_nodes.copy()
        tmax = np.ones((self.k_routes,1))*self.B_time_budget
        tmax = tmax.tolist()

        
              
        while True:
            for m in range(self.k_routes):
                
                SV_nodes = self.sorted_valid_nodes(node_0=Ym[m][-1], nodes = np.array(SV_nodes)[:,0].astype(int),Tmax = tmax[m])
                print(f"Nodos válidos: {SV_nodes}\n")
                
                Ym[m].append(SV_nodes.pop()[0])
                
                
                t_consumed[m] = t_consumed[m] + self.distances[Ym[m][-1], Ym[m][-2]]
                print(f"Tiempo consumido: {t_consumed}\n")
                
                tmax[m] = tmax[m] - t_consumed[m]
                print(f"Tiempo que queda: {tmax}\n")
            
            print(Ym)
        
        
        
        #nodes_profits = sorted(nodes_profits[0], key = lambda pf : pf[1])
        

            
                
        
        
        

top_1 = TOP("C:/Users/Andres Prieto/Documents/Master Investigación en Inteligencia Artificial/Resolución de Problemas con Metaheurísticos/Trabajo/Team_Orienteering_Problem/TOP_Inst/Set_21_234/p2.2.a.txt")
        
# print(top_1.get_data())
# print(top_1.get_data(mode="list"))

tmax, n, m, nodes, coor_x, coor_y, coor, profit, edges = top_1.get_data(mode="list")

#print(top_1.nodes_out_Tmax(0))


top_1.draw()

top_1.inicialization()

print(top_1.distances(0,13) + top_1.distances(13,10) + top_1.distances(10,20))

# print(top_1.sorted_valid_nodes())
# print(top_1.nodes)



























