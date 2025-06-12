# 🧮 Codezelle: Ungerichteter Graph
import networkx as nx
import matplotlib.pyplot as plt

# 🧮 Codezelle: Gerichteter Graph (Digraph)
G2 = nx.DiGraph()
G2.add_edges_from([("B", "L"), ("L", "DD"), ("DD", "B"), ("DD", "Löb")])

plt.figure(figsize=(4, 3))
nx.draw(G2, with_labels=True, node_color='lightcoral', edge_color='black',
        node_size=800, arrows=True, arrowstyle='->', arrowsize=20)
plt.title("Abb. 4: Gerichteter Graph (Digraph)")
plt.show()