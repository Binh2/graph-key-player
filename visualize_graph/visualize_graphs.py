from typing import Callable
import networkx as nx
from matplotlib import pyplot as plt
from .visualize_graph import visualize_graph, visualize_node_feature_graph, visualize_edge_feature_graph


def get_sizes():
  return ({
    1: {"nrows": 1, "ncols": 1},
    2: {"nrows": 2, "ncols": 1},
    3: {"nrows": 2, "ncols": 2},
    4: {"nrows": 2, "ncols": 2},
    5: {"nrows": 2, "ncols": 3},
    6: {"nrows": 2, "ncols": 3},
    7: {"nrows": 2, "ncols": 4},
    8: {"nrows": 2, "ncols": 4},
    9: {"nrows": 3, "ncols": 3},
  })

def visualize_graphs(Gs: list[nx.Graph | nx.DiGraph], 
                     display_label: bool = True, 
                     layout: Callable = nx.spring_layout):
  sizes = get_sizes()
  fig, axes = plt.subplots(**sizes[len(Gs)])
  ax = axes.flatten()
  for i in range(len(Gs)):
    G = Gs[i]
    pos = layout(G)
    ax[i].set_xlabel(str(i+1))
    visualize_graph(G, display_label, ax[i], layout)

  plt.show()


def visualize_node_feature_graphs(Gs: list[nx.Graph], features, display_label=True, layout=nx.spring_layout):
  sizes = get_sizes()
  fig, axes = plt.subplots(**sizes[len(Gs)])
  ax = axes.flatten()
  for i in range(len(Gs)):
    G = Gs[i]
    pos = layout(G)
    ax[i].set_xlabel(str(i+1))
    visualize_node_feature_graph(G, features, display_label, ax=ax[i])
  plt.show()


def visualize_edge_feature_graphs(Gs: list[nx.Graph], features, display_label=True, layout=nx.spring_layout):
  sizes = get_sizes()
  fig, axes = plt.subplots(**sizes[len(Gs)])
  ax = axes.flatten()
  for i in range(len(Gs)):
    G = Gs[i]
    pos = layout(G)
    ax[i].set_xlabel(str(i+1))
    visualize_edge_feature_graph(G, features, display_label, ax=ax[i])
  plt.show()