import networkx as nx
from load_twitter import load_twitter


def load_custom_graph(type: int):
  '''type = 1 | 2 | 3 | 11 | 12 | 13 | 14 | 15 | 16 | 17. 
  Type 1 and 2 are undirected graph. 
  Type 3 is a directed graph.
  Type 11 through 17 is loaded from twitter data. With type 11 is 10 edge, type 12 is 100 edge and so on
  '''
  G = nx.Graph()
  if type == 1:
    G.add_edges_from([(1, 2), (1, 5), (2, 3), (2, 5), (3, 4), (4, 5), (4, 6)])

  elif type == 2:
    G.add_edges_from([
      (1, 2), (1, 3), (1, 4),
      (2, 3),
      (3, 4),
      (4, 5), (4, 6),
      (5, 6), (5, 7), (5, 8),
      (6, 7), (6, 8),
      (7, 8), (7, 9),
    ])
  elif type == 3:
    G = nx.DiGraph()
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 2), (3, 4), (4, 5), (4, 6)])
  elif type == 11:
    G = load_twitter(number_of_edges=10)
  elif type == 12:
    G = load_twitter(number_of_edges=100)
  elif type == 13:
    G = load_twitter(number_of_edges=1000)
  elif type == 14:
    G = load_twitter(number_of_edges=10000)
  elif type == 15:
    G = load_twitter(number_of_edges=100000)
  elif type == 16:
    G = load_twitter(number_of_edges=1000000)
  elif type == 17:
    G = load_twitter()
  
  return G


if __name__ == "__main__":
  from visualize_graph import visualize_graph, visualize_graphs, interactively_visualize_graph
  from argparse import ArgumentParser
  argParser = ArgumentParser("Load custom graph")
  argParser.add_argument("-g", "--graphs", default=[1,2,3,11,12,13], nargs='+', type=int, help="Add the graph type here to display it")
  argParser.add_argument("-i", "--interactive", action="store_true", help="Draw network graph in interactive mode")
  args = argParser.parse_args()
  print(args.interactive)
  if not args.interactive:
    if len(args.graphs) > 1:
      Gs = []
      for i in args.graphs:
        Gs.append(load_custom_graph(i))
      visualize_graphs(Gs, layout=nx.kamada_kawai_layout)
    elif len(args.graphs) == 1:
      visualize_graph(load_custom_graph(args.graphs[0]), display_label=False, node_size=50, layout=nx.kamada_kawai_layout)
  else:
    if len(args.graphs) >= 1:
      interactively_visualize_graph(load_custom_graph(args.graphs[0]))