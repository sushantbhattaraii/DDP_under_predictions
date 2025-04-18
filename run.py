from collections import defaultdict, deque
from final_tree_T import *
from tree_center import find_tree_center
import random
import networkx as nx
import network_generator as my_ng
import argparse
import matplotlib.pyplot as plt


request_queue = defaultdict(deque)
global link_
link_ = None


def build_parent_dict(T, root):
    """
    Perform a BFS (or DFS) from 'root' in the tree T to define
    a parent-child relationship. 
    Returns a dict 'parent' where parent[u] = node's parent in T 
    (with root having parent[root] = None).
    """
    parent = {root: None}
    queue = deque([root])
    
    while queue:
        current = queue.popleft()
        for neighbor in T.neighbors(current):
            if neighbor not in parent:  # not visited
                parent[neighbor] = current
                queue.append(neighbor)
    return parent


def publish(T, o, root, parent, link_):
    """
    Implements Algorithm 1 (Publish) from your snippet.
    
    Parameters:
    -----------
    T      : networkx.Graph (tree)
    o      : The node that currently receives/owns the resource.
    root   : The designated root of T.
    parent : dict, mapping each node to its parent in T.
    link_  : dict, mapping each node to link[node]. 
             This function modifies link_ in place.
    
    After publish(), for each node ui on the path from o up to (but not including) root,
    we set link(ui) = child, where 'child' is the node from which the publish message arrived.
    """
    u = o
    # ui = parent[u]
    ui = parent.get(u, None)  # Use .get() to avoid KeyError
    
    # Climb up the tree until we reach the root
    while ui is not None:
        link_[ui] = u
        # Move up one level
        u = ui
        # ui = parent[u]
        ui = parent.get(u, None)  # Use .get() to avoid KeyError
        # print("U->", u, "ui->",ui)
        if(u == root):
            break
    # The loop stops when ui == root or ui == None.
    # By the pseudocode, we do NOT set link(root) in the final step.


def set_links_for_request(G, T, requesting_node, parent, link_, root):
    """
    For a requesting node r:
    1) Set link_[r] = r.
    2) Climb up from r to root, flipping pointers so that link_[p] = child,
       where p is the parent and child is the node from which the request came.
    3) After establishing these links on the path, set all other links to None.
    """
    # Keep track of the path from requesting_node to root
    path_nodes = []


    for node, value in link_.items():
        if value == node:
            owner = node

    dist_u_v_in_T = nx.shortest_path_length(T, source=owner, target=requesting_node, weight='weight')

    dist_u_v_in_G = nx.shortest_path_length(G, source=owner, target=requesting_node, weight='weight')

    # stretch = float(dist_u_v_in_T / dist_u_v_in_G)
    
    # Step 1: requesting_node points to itself
    link_[requesting_node] = requesting_node
    path_nodes.append(requesting_node)
    
    # Step 2: climb upwards until we reach the root
    current = requesting_node
    while current != root:
        p = parent[current]
        # If there's no parent (i.e., current is already root), break
        if p is None:
            break
        link_[p] = current  # flip pointer
        path_nodes.append(p)
        current = p
    
    # Step 3: For all other nodes NOT on this path, set link_[node] = None
    for node in link_.keys():
        if node not in path_nodes:
            link_[node] = None

    return dist_u_v_in_G, dist_u_v_in_T

def load_graph():
    # graph_name = my_ng.build_graphs()
    # graphml_file = graph_name
    graphml_file = '.\\graphs\\1024random_diameter24test.edgelist'
    G_example = nx.read_graphml(graphml_file)
    G_example = nx.relabel_nodes(G_example, lambda x: int(x))
    return G_example


def calculate_stretch(G_example, T, Vp, fraction, owner):
    # V is the set of all vertices in the graph G.
    V = list(T.nodes())

    # Requesting nodes Q: randomly select 1/4th of V with the same cardinality as Vp,
    # also ensuring they do not include the owner.
    available_for_Q = list(set(V) - {owner})
    Q = random.sample(available_for_Q, len(Vp))

    print("Total # of vertices (n): ", len(V))
    print("Total vertices (V):", V)
    print("Fraction used:", fraction)
    print("Predicted vertices (Vp):", Vp)
    print("Requesting nodes (Q):", Q)
    print("\n--- Move Operations ---")

    centers = find_tree_center(T)
    # print("Center(s) of the tree:", centers)

    root = centers[0]
    print("Root node of the final tree T:", root)

    parent = build_parent_dict(T, root)

    # Initialize link[u] = None for all nodes u
    link_ = {u: None for u in T.nodes()}
    
    # Optionally, you might set link[owner] = owner if you want
    # to indicate that the owner points to itself.
    link_[owner] = owner
    
    # print("Initial parent dictionary:", parent)
    # print("Initial link:", link_)
    
    # Run publish() from owner = 5
    publish(T, owner, root, parent, link_)
    
    print("\nAfter running publish() from owner")
    print("Updated link:", link_)

    distances_in_G = []
    distances_in_T = []
    for r in Q:
        # print(f"\nRequest from node {r} ... ")
        d_in_G, d_in_T = set_links_for_request(G_example, T, r, parent, link_, root)
        # stretch_i = float(d_in_T) / d_in_G if d_in_G != 0.0 else float('inf')
        distances_in_G.append(d_in_G)
        distances_in_T.append(d_in_T)
        # print(f"\nDistance between request node {r} and owner node in T is {d_in_T}, stretch = {stretch_i:.4f}")

        # print("Updated link_ after request:")
        # for node in sorted(T.nodes()):
        #     print(link_)

    # print("Distances in G: ")
    # print(distances_in_G)
    # print("Distances in T: ")
    # print(distances_in_T)
    sum_of_distances_in_G = sum(distances_in_G)
    sum_of_distances_in_T = sum(distances_in_T)
    stretch = sum_of_distances_in_T / sum_of_distances_in_G if sum_of_distances_in_G != 0 else float('inf')
    # print("Type of distances in G:", type(distances_in_G))
    # print("Type of distances in T:", type(distances_in_T))
    # stretch = max(stretches) if stretches else 0
    GREEN = "\033[92m"
    RESET = "\033[0m"
    print(f"{GREEN}\nStretch (sum_of_distance_in_T / sum_of_distance_in_G) = {stretch}{RESET}")
    return Q


def calculate_error(Q, Vp, G_example, diameter_of_G, diameter_of_T):
    errors = []
    for req, pred in zip(Q, Vp):
        # Using NetworkX to compute the shortest path length in tree T.
        dist = nx.shortest_path_length(G_example, source=req, target=pred, weight='weight')
        error = dist / diameter_of_G
        errors.append(error)
        # print(f"\nDistance between request node {req} and predicted node {pred} is {dist}, error = {error:.4f}")
    
    print("Diameter of G:", diameter_of_G)
    print("Diameter of T:", diameter_of_T)
    total_error = max(errors) if errors else 0
    RED = "\033[91m"
    RESET = "\033[0m"
    print(f"{RED}\nOverall error (max_i(distance_in_G / diameter_G)) = {total_error:.4f}{RESET}")
    return total_error


def main(fraction):

    G_example = load_graph()

    # show_graph(G_example)

    diameter_of_G = nx.diameter(G_example, weight='weight')
    print("Diameter of G_example:", diameter_of_G)

    S_example, Vp, owner = choose_steiner_set(G_example, fraction)
    print("Randomly chosen Predicted Vertices (Vp):", Vp)
    print("Owner node:", owner)
    # print("Steiner set S:", S_example)

    # Compute Steiner tree
    T_H = steiner_tree(G_example, S_example)

    # Print edges of the resulting Final tree
    # print("Final Tree edges:")
    # for (u, v, data) in T_H.edges(data=True):
    #     print(f"{u} - {v}, weight = {v['weight'] if isinstance(v, dict) else v}")

    # Compute Final tree T
    T = augment_steiner_tree_with_remaining_vertices(G_example, T_H)

    # verifying the edge weights by printing them
    # for u, v, weight in T.edges(data='weight'):
    #     print(f"Edge ({u}, {v}) has weight: {weight}")

    # show_graph(T)

    Q = calculate_stretch(G_example, T, Vp, fraction, owner)

    diameter_of_T = nx.diameter(T, weight='weight')

    total_error = calculate_error(Q, Vp, G_example, diameter_of_G, diameter_of_T)

    return total_error


if __name__ == "__main__":
    errros_to_plot = []
    p = argparse.ArgumentParser(description="Running the experiment with different fractions of predicted nodes ... ")
    p.add_argument(
        "--fraction",
        type=float,
        required=True,
        help="The fraction of nodes to pick as Vp (e.g. 0.0625, 0.125, 0.25, 0.5)"
    )
    args = p.parse_args()
    main(args.fraction)

    


    
    

