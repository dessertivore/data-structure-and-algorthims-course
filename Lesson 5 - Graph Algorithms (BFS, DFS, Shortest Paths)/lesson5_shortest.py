"""
Question: Write a function to find the length of the shortest path between two nodes in 
a weighted directed graph.
If a graph is not weighted, shortest path is found with BFS.

Dijkstra's Algorithm finds the shortest path between a given node 
("source node") and all other nodes in a graph.

Code below from udacity, edited to work with my graph class
"""

from lesson5_weighted import WeightedEdgeGraph, g7


def dijkstra_algorithm(graph: WeightedEdgeGraph, start_node: int):
    unvisited_nodes = set(range(graph.num_nodes))
    # create list of shortest paths, and initialize value of the unvisited nodes as infinity
    shortest_path = {node: float("inf") for node in range(graph.num_nodes)}
    # However, we initialize the starting node's value with 0
    shortest_path[start_node] = 0

    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {node: None for node in range(graph.num_nodes)}

    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes:  # Iterate over the nodes
            if (
                current_min_node == None
                or shortest_path[node] < shortest_path[current_min_node]
            ):
                current_min_node = node
                # retrieve the current node's neighbors
                neighbours = graph.data[current_min_node]
        # update distances for neighbours - weight of edge + current distance to get there
        for neighbour in neighbours:
            # extract weight for neighbour node edge
            for neighbour_node, neighbour_weight in graph.weight[current_min_node]:
                if neighbour_node == neighbour:
                    weight = neighbour_weight

            if weight is not None:
                tentative_value = shortest_path[current_min_node] + weight
                if tentative_value < shortest_path[neighbour]:
                    shortest_path[neighbour] = tentative_value
                    # We also update the best path to the current node
                    previous_nodes[neighbour] = current_min_node

        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path


print(dijkstra_algorithm(g7, 5))
