import networkx as nx
import matplotlib.pyplot as plt

def show_graph(G):
    # Load the graph from a GraphML file
    # graphml_file = '.\\graphs\\10random_diameter2test.edgelist'
    # G = nx.read_graphml(graphml_file)

    # Generate a layout for the nodes
    pos = nx.spring_layout(G)

    edge_weight = nx.get_edge_attributes(G, 'weight')


    # Draw the graph with labels
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weight)


    # Add a title to the graph
    plt.title("GraphML Graph Visualization")

    # Display the graph
    plt.show()



