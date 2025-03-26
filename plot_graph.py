import networkx as nx
import matplotlib.pyplot as plt

# Load the graph from a GraphML file
graphml_file = '.\\graphs\\10random_diameter3test.edgelist'
G = nx.read_graphml(graphml_file)

# Generate a layout for the nodes
pos = nx.spring_layout(G)

# Draw the graph with labels
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500)

# Add a title to the graph
plt.title("GraphML Graph Visualization")

# Display the graph
plt.show()
