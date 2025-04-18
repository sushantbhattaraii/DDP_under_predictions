import networkx as nx
import matplotlib.pyplot as plt
import os
import re

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


def plot_error_graph(fraction, errors_to_plot, file_name):

    x = fraction
    y = errors_to_plot

    numbers_in_filename = re.findall(r'\d+\.?\d*', file_name)
    total_number_of_nodes_in_graph = str(numbers_in_filename[0])

    # print(type(x), type(y))
    # exit(0)

    plt.figure()
    plt.plot(x, y, marker='o', linestyle='-')
    plt.xlabel('Fraction of Predicted Nodes/#of operations')
    plt.ylabel('Error')
    plt.title('# of operations vs Error Graph | Number of nodes: '+ total_number_of_nodes_in_graph)
    plt.grid(True)
    folder_name = "results"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    path_to_save = os.path.join('results', 'error_graphs', file_name)
    plt.savefig(path_to_save)
    plt.show()
