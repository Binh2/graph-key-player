import networkx as nx
from pyvis.network import Network


def interactively_visualize_graph(G: nx.Graph | nx.DiGraph, filename: str = "network.html"):
  nt = Network()
  nt.from_nx(G)
  nt.show(filename, notebook=False)