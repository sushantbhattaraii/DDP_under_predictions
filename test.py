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
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]

plt.figure()
plt.plot(x, y, marker='o', linestyle='-')
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Sample 2D Plot')
plt.grid(True)
plt.show()

