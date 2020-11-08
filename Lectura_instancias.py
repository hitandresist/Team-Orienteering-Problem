import networkx as nx
import matplotlib.pyplot as plt
import itertools as itools

class Instancia_OP():
    """En este objeto se guardan los datos necesarios para
    instanciar el Orienteering Problem. Los lee desde un
     fichero txt con un formato determinado.

     El origen de los mismos los pueden encontrar en
     https://www.mech.kuleuven.be/en/cib/op, así como una
     explicación detallada del significado de cada uno de
     los valores"""
    read_file()

    def __init__(self, filepath):
        self.fieldpath = filepath
        self.instance_data = open(self.filepath)
        self.time_budget = ""
        self.N_nodes = ""
        self.coor_x = ""
        self.coor_y = ""
        self.nodes = ""
        self.edges = ""

        pass
