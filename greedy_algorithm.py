from typing import Callable
import networkx as nx


def greedy_algorithm(G: nx.Graph | nx.DiGraph, key_player_function: Callable[[nx.Graph | nx.DiGraph, set], float], k: int):
  '''k is the number of nodes inside the key player set'''
  node_set = set(G.nodes)
  node_set_len = len(node_set)
  if node_set_len < k: raise Exception('k must be less than or equal to number of nodes in Graph')

  key_player_set = set(G.nodes[:k])
  remainder_set = node_set - key_player_set
  fit = key_player_function(G, key_player_set)
  for u in key_player_set:
    remainder_set
