from collections import defaultdict, deque

# --------------------------------------------------------
# Setup Data Structures
# --------------------------------------------------------

# Suppose we have a tree of N nodes labeled 1..N (for example).
# parent[node] gives the parent of 'node' in the tree (None if node is root).
parent = {}
children = defaultdict(list)

# link[node]: the "arrow" or pointer that indicates where the node believes the resource is.
# If link[node] = node, it means node is the terminal (owner or waiting for the resource).
# If link[node] = some_other_node, it means the resource is believed to be in that direction.
# If link[node] = None, the node has no information.
link_ = {}

# For demonstration, we store the "owner" of object o in a single variable.
# If you have multiple objects, you might store owner(o) in a dictionary.
owner_node = None

# Each node has a request_queue for move() requests, though concurrency is not fully shown here.
request_queue = defaultdict(deque)

# --------------------------------------------------------
# Example Initialization
# --------------------------------------------------------
def initialize_tree(nodes, root=1):
    """
    A simple helper that sets up parent/children/link_ for a given tree.
    This is just for illustration; you can adapt to your existing data.
    """
    global parent, children, link_, owner_node

    # For simplicity, assume 'nodes' is a list of (node, par) giving each node's parent
    # or None if it is root. Or do your own method to build the tree.
    for (n, p) in nodes:
        parent[n] = p
        if p is not None:
            children[p].append(n)

        # Initialize link so that they point to the current owner if known.
        # For now, set them all to None or themselves, adapt as needed.
        link_[n] = None

    # Suppose the owner is the root at the start. 
    owner_node = root
    link_[root] = root  # The owner points to itself.


# --------------------------------------------------------
# Core Move Operation (Algorithm 3)
# --------------------------------------------------------

def move_request(o, current_node, from_node):
    """
    Processes a move(o) message that arrived at 'current_node' from 'from_node'.
    The goal: eventually get the resource o to the requesting node (somewhere in the path).
    
    This function implements a simplified version of "Algorithm 3 Move()" from your description.
    """

    global owner_node

    # 1. If current_node is the owner, handle the request:
    if current_node == owner_node:
        # Enqueue the request (simplified: we just place it in a queue)
        request_queue[current_node].append(from_node)

        # Wait until current_node finishes with 'o' (abstracted away)
        # ... do some writing or modification ...
        # Once done, it can send a writable copy of 'o' to from_node:

        # In a real implementation, you'd have concurrency control, etc.
        # For now, just simulate that we are done and we send 'o'.
        # "remove the read-only copies" is also protocol-dependent, omitted here.
        
        # Dequeue the request
        _ = request_queue[current_node].popleft()

        # The resource moves to from_node
        # => from_node becomes new owner (or at least it receives the exclusive copy)
        owner_node = from_node
        link_[from_node] = from_node  # Now the new node points to itself

        # (Optionally) the old owner can set link_[current_node] = from_node or None
        # depending on how you handle the pointer flips in your code.
        link_[current_node] = from_node

        # Move is done at this point for the requesting node.
        return

    # 2. If current_node is NOT the owner, check if link(current_node) = None
    if link_[current_node] is None:
        # If link is NULL, we set link(current_node) = from_node,
        # and send move(o) upward to parent(current_node)
        link_[current_node] = from_node

        p = parent[current_node]
        if p is not None:
            # Send move(o) to the parent
            move_request(o, p, current_node)
        else:
            # current_node is root but not the owner? 
            # Then we have a corner case. 
            # In many protocols, the root would eventually lead to the owner, 
            # or the root might itself be the owner. 
            # For demonstration, we do nothing or handle as needed.
            pass

    else:
        # 3. If link(current_node) is not None, forward the request to link(current_node).
        # Let v = link(current_node).
        v = link_[current_node]

        # "send move(o) to link(ui)"
        move_request(o, v, current_node)

        # After sending, check if v is the root of T (or some special condition):
        # The pseudocode snippet says:
        #   if v = root of T then
        #       link(ui) = u
        #   else
        #       link(ui) = NULL
        # Here, 'u' is the node from which the request came in the snippet. 
        # In our code, that is 'from_node'.

        if v == find_root(current_node):
            # Suppose find_root(...) is a helper that returns the root of the tree
            link_[current_node] = from_node
        else:
            link_[current_node] = None


def find_root(node):
    """
    Helper to return the root of the tree containing 'node'
    by following parent pointers until None.
    """
    cur = node
    while parent[cur] is not None:
        cur = parent[cur]
    return cur


# --------------------------------------------------------
# DEMO USAGE
# --------------------------------------------------------
if __name__ == "__main__":
    # Build a small tree with 5 nodes, root = 1
    # Suppose the structure is:
    #    1
    #   / \
    #  2   3
    #     / \
    #    4   5
    tree_structure = [
        (1, None),  # 1 is root
        (2, 1),
        (3, 1),
        (4, 3),
        (5, 3),
    ]
    initialize_tree(tree_structure, root=1)

    # Let's say node 1 is initially the owner of object o:
    obj = "o"

    # Node 4 wants to move(o) for writing:
    # We simulate node 4 sending the request to its parent (3).
    move_request(obj, 3, 4)

    # In a real system, the request travels up to the owner (node 1),
    # the owner eventually sends the object down to node 4,
    # making node 4 the new owner. 
    print("Final owner of o is:", owner_node)
    # Check link array
    print("Links after the move operation:")
    for n in sorted(link_.keys()):
        print(f"  link[{n}] = {link_[n]}")
