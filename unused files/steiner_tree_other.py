import networkx as nx
import random
import matplotlib.pyplot as plt

def load_graph(filename):
    """
    Load a graph from a GraphML file.
    """
    return nx.read_graphml(filename)

def choose_steiner_set(G):
    """
    Randomly choose Vp (1/3 of all nodes) as Steiner points,
    and then choose one additional 'owner' node not in Vp.
    Return the set S = Vp ∪ {owner}, along with Vp and owner.
    """
    nodes = list(G.nodes())
    total_nodes = len(nodes)
    vp_size = total_nodes // 3  # using integer division for 1/3 of nodes
    Vp = set(random.sample(nodes, vp_size))
    
    # Choose an owner node that is not in Vp
    remaining = set(nodes) - Vp
    owner = random.choice(list(remaining))
    
    S = Vp.union({owner})
    return S, Vp, owner

def construct_complete_graph(G, S):
    """
    Construct a complete graph on the vertex set S.
    The weight of edge {u,v} is the shortest path distance between u and v in G.
    """
    complete_G = nx.Graph()
    for u in S:
        complete_G.add_node(u)
    S_list = list(S)
    for i in range(len(S_list)):
        for j in range(i+1, len(S_list)):
            u, v = S_list[i], S_list[j]
            try:
                # Compute the shortest path length in G (using weights if available)
                length = nx.shortest_path_length(G, source=u, target=v, weight='weight')
            except nx.NetworkXNoPath:
                length = float('inf')
            complete_G.add_edge(u, v, weight=length)
    return complete_G

def steiner_tree_heuristic(G, S):
    """
    Apply the heuristic algorithm to construct a Steiner tree on S ⊆ V.
    Algorithm Steps:
      1. Build complete graph G' on S with distances from G.
      2. Compute the MST T1 of G'.
      3. For each edge in T1, replace it with the corresponding shortest path in G to form Gs.
      4. Compute the MST Ts of Gs.
      5. Prune Ts so that every leaf is in S.
    Returns the final Steiner tree Tn.
    """
    # Step 1: Construct complete graph G' on S.
    complete_G = construct_complete_graph(G, S)
    
    # Step 2: Find the minimal spanning tree T1 of G'.
    T1 = nx.minimum_spanning_tree(complete_G)
    
    # Step 3: Construct subgraph Gs by replacing each edge in T1 by its shortest path in G.
    Gs = nx.Graph()
    for (u, v, data) in T1.edges(data=True):
        path = nx.shortest_path(G, source=u, target=v, weight='weight')
        # Add all edges along the path to Gs with their original weights from G.
        for i in range(len(path) - 1):
            a, b = path[i], path[i+1]
            weight = G[a][b].get('weight', 1)  # default weight is 1 if not specified
            Gs.add_edge(a, b, weight=weight)
    
    # Step 4: Find the minimal spanning tree Ts of Gs.
    Ts = nx.minimum_spanning_tree(Gs)
    
    # Step 5: Prune Ts so that every leaf is in S.
    Tn = prune_tree(Ts, S)
    return Tn

def prune_tree(T, S):
    """
    Prune the tree T by iteratively removing leaves that are not in S,
    until all leaves are in S.
    """
    T_pruned = T.copy()
    removed = True
    while removed:
        removed = False
        # Identify leaves (nodes with degree 1).
        leaves = [node for node in T_pruned.nodes() if T_pruned.degree(node) == 1]
        for leaf in leaves:
            if leaf not in S:
                T_pruned.remove_node(leaf)
                removed = True
    return T_pruned

def main():
    # Load the graph from a GraphML file.
    filename = ".\\graphs\\10random_diameter3test.edgelist" # Change this to your GraphML file name.
    G = load_graph(filename)
    
    # Choose the Steiner set S = Vp ∪ {owner}
    S, Vp, owner = choose_steiner_set(G)
    print("Randomly chosen Predicted Vertices (Vp):", Vp)
    print("Owner node:", owner)
    print("Steiner set S:", S)
    
    # Construct the Steiner tree using the heuristic algorithm.
    steiner_tree = steiner_tree_heuristic(G, S)
    
    # Draw and display the resulting Steiner tree.
    pos = nx.spring_layout(steiner_tree)  # Compute layout for visualization
    plt.figure(figsize=(8, 6))
    nx.draw_networkx(steiner_tree, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.title("Heuristic Steiner Tree on S (Vp ∪ {owner})")
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    main()
