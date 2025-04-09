from collections import defaultdict, deque
from final_tree_T import *
from tree_center import find_tree_center
import random
import networkx as nx


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


def set_links_for_request(requesting_node, parent, link_, root):
    """
    For a requesting node r:
    1) Set link_[r] = r.
    2) Climb up from r to root, flipping pointers so that link_[p] = child,
       where p is the parent and child is the node from which the request came.
    3) After establishing these links on the path, set all other links to None.
    """
    # Keep track of the path from requesting_node to root
    path_nodes = []
    
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



if __name__ == "__main__":
    # fraction of nodes to be chosen as Vp
    global fraction
    fraction = float(1/4)

    graphml_file = '.\\graphs\\'+'10random_diameter6test.edgelist'
    G_example = nx.read_graphml(graphml_file)
    G_example = nx.relabel_nodes(G_example, lambda x: int(x))

    S_example, Vp, owner = choose_steiner_set(G_example, fraction)
    print("Randomly chosen Predicted Vertices (Vp):", Vp)
    print("Owner node:", owner)
    print("Steiner set S:", S_example)

    # Compute Steiner tree
    T_H = steiner_tree(G_example, S_example)

    # Print edges of the resulting Final tree
    print("Final Tree edges:")
    for (u, v, data) in T_H.edges(data=True):
        print(f"{u} - {v}, weight = {v['weight'] if isinstance(v, dict) else v}")

    # Compute Final tree T
    T = augment_steiner_tree_with_remaining_vertices(G_example, T_H)
    show_graph(T)
    total_nodes = len(G_example)

    # V is the set of all vertices in the graph G.
    V = list(T.nodes())

    # Requesting nodes Q: randomly select 1/4th of V with the same cardinality as Vp,
    # also ensuring they do not include the owner.
    available_for_Q = list(set(V) - {owner})
    Q = random.sample(available_for_Q, len(Vp))


    print("Total vertices (V):", V)
    print("Owner node:", owner)
    print("Fraction used:", fraction)
    print("Predicted vertices (Vp):", Vp)
    print("Requesting nodes (Q):", Q)
    print("\n--- Move Operations ---")

    centers = find_tree_center(T)
    print("Center(s) of the tree:", centers)

    root = centers[0]
    print("Root node of the final tree:", root)

    parent = build_parent_dict(T, root)

    # Initialize link[u] = None for all nodes u
    link_ = {u: None for u in T.nodes()}
    
    # Optionally, you might set link[owner] = owner if you want
    # to indicate that the owner points to itself.
    link_[owner] = owner
    
    print("Initial parent dictionary:", parent)
    print("Initial link:", link_)
    
    # Run publish() from owner = 5
    publish(T, owner, root, parent, link_)
    
    print("\nAfter running publish() from owner")
    print("Updated link:", link_)

    for r in Q:
        print(f"\nRequest from node {r} ... ")
        set_links_for_request(r, parent, link_, root)
        
        print("Updated link_ after request:")
        for node in sorted(T.nodes()):
            print(f"  link_[{node}] = {link_[node]}")


    
    

