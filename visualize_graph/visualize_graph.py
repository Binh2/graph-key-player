from typing import Callable
import networkx as nx
from matplotlib import pyplot as plt


def visualize_graph(G: nx.Graph, 
                    display_label: bool = True, 
                    node_size: int = 300,
                    ax = None, 
                    layout: Callable = nx.spring_layout):
  pos = layout(G)
  # nx.draw_networkx_nodes(G, pos, ax=ax)
  # if display_label: nx.draw_networkx_labels(G, pos, ax=ax)
  # nx.draw_networkx_edges(G, pos, ax=ax)
  nx.draw(G, pos=pos, with_labels=display_label, node_size=node_size, ax=ax)
  plt.show()


def visualize_node_feature_graph(G: nx.Graph | nx.DiGraph, 
                                 features: dict, 
                                 display_label: bool = True, 
                                 ax = None, 
                                 layout: Callable = nx.spring_layout):
  pos = layout(G)
  nx.draw(G, pos=pos, with_labels=display_label, ax=ax)
  nx.draw_networkx_labels(G, pos={node: (p[0]+.05, p[1]+.05) for node, p in pos.items()}, labels=features, ax=ax)
  plt.show()


def visualize_edge_feature_graph(G: nx.Graph | nx.DiGraph, 
                                 features: dict, 
                                 display_label: bool = True, 
                                 ax = None, 
                                 layout: Callable = nx.spring_layout):
  pos = layout(G)
  nx.draw(G, pos=pos, with_labels=display_label, ax=ax)
  edge_pos = {}
  shift = 0.01
  for edge in G.edges:
    edge_pos[edge] = ((pos[edge[0]][0] + pos[edge[1]][0])/2 + shift, (pos[edge[0]][1] + pos[edge[1]][1])/2 + shift)
  nx.draw_networkx_labels(G, pos=edge_pos, labels=features, ax=ax)
  plt.show()
