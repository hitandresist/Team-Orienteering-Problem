import networkx as nx
import matplotlib.pyplot as plt
import itertools as itools

nodes = [1, 2, 3, 4, 5]
edges = list(itools.combinations(nodes, 2))
print(edges)

for i in edges:
    print(i)


G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)


plt.plot(1)
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()