import networkx as nx


def pos_key_player_centrality(G: nx.Graph | nx.DiGraph, key_player_set: set) -> float:
  node_set = set(G.nodes)
  node_set_len = len(node_set)
  remainder_set = node_set - key_player_set

  shortest_path = nx.algorithms.all_pairs_shortest_path(G)
  reach_centrality = 0 
  for j in remainder_set:
    min_distance = node_set_len - 1
    for i in key_player_set:
      distance = len(shortest_path[i][j])
      if min_distance > distance:
        min_distance = distance
    
    reach_centrality += distance
  
  reach_centrality /= node_set_len
  return reach_centrality

    
