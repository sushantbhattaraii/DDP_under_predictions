#importing the networkx library
# import networkx as nx

# #importing the matplotlib library for plotting the graph
# import matplotlib.pyplot as plt

# G = nx.erdos_renyi_graph(10,0.1)
# print(nx.is_connected(G))
# nx.draw(G, with_labels=True)
# plt.show()


import matplotlib.pyplot as plt

# Example data for x and y axes
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 1, 8, 7]

# plt.figure()
# plt.plot(x, y, marker='o', linestyle='-')
# plt.xlabel('X-axis label')
# plt.ylabel('Y-axis label')
# plt.title('Sample 2D Plot')
# plt.grid(True)
# plt.show()



# import networkx as nx

# G = nx.read_graphml(".\\graphs\\256random_diameter71test.edgelist")

# # Gather all data‐keys present on edges
# edge_keys = {
#     k
#     for u, v, data in G.edges(data=True)
#     for k in data.keys()
# }

# if "weight" in edge_keys:
#     print("✓ Found an edge attribute named 'weight'")
# else:
#     print("✗ No 'weight' attribute on any edge")
    
# # (you can also print edge_keys to see other attributes)
# print("All edge attributes:", edge_keys)


import matplotlib.pyplot as plt

# Create the plot
fig, ax = plt.subplots()

# Set y-ticks
y_ticks = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
for i in range(1, 41):
    y_ticks.append(1 + i * 0.1)

ax.set_yticks(y_ticks)
ax.set_ylim(0.0, 4.0)  # Set y-axis limits to match ticks

# Add a dummy plot to prevent matplotlib from automatically setting the y-ticks
ax.plot([0], [0], color='white')

# Show the plot
plt.show()
