import networkx as nx
import matplotlib.pyplot as plt
import itertools as itools

nodes = [1, 2, 3, 4, 5]
edges = list(itools.combinations(nodes, 2))

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

plt.plot(1)
nx.draw(G, pos = { 1 : (0,0), 2 : (0,1),3 : (2,0),4 : (2,2),5 : (3,2)} , with_labels=True, font_weight='bold')
plt.show()



