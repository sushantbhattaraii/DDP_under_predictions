from collections import defaultdict, deque
from final_tree_T import *

if __name__ == "__main__":

    graphml_file = '.\\graphs\\'+'10random_diameter6test.edgelist'
    G_example = nx.read_graphml(graphml_file)
    G_example = nx.relabel_nodes(G_example, lambda x: int(x))

    S_example, Vp, owner = choose_steiner_set(G_example)
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
    print("Predicted vertices (Vp):", Vp)
    print("Requesting nodes (Q):", Q)
    print("\n--- Move Operations ---")

    
    
    

