# 🧮 Codezelle: Ungerichteter Graph
import networkx as nx
import matplotlib.pyplot as plt

# Ungerichteter Graph
G1 = nx.Graph()
G1.add_edges_from([(1, 2), (1, 3), (2, 4)])

plt.figure(figsize=(4, 3))
nx.draw(G1, with_labels=True, node_color='lightgreen', edge_color='gray', node_size=800)
plt.title("Abb. 3: Einfacher Graph")
plt.show()