import networkx as nx
import matplotlib.pyplot as plt

def show_graph(G):
    # Load the graph from a GraphML file
    # graphml_file = '.\\graphs\\10random_diameter2test.edgelist'
    # G = nx.read_graphml(graphml_file)

    # Position nodes for better visualization
    pos = nx.spring_layout(G)

    # Draw nodes
    nx.draw_networkx_nodes(G, pos)

    # Draw edges
    nx.draw_networkx_edges(G, pos)

    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # # Draw node labels
    nx.draw_networkx_labels(G, pos)

    # Show the plot
    plt.show()