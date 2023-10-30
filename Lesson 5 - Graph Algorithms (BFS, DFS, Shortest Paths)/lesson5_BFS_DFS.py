"""
Create a class to represent a graph as an adjacency list in Python.
Use code from tutor to make adjacency lit class, then added myself the 
functions to remove and add edges
"""

from typing import Any


num_nodes1 = 5
edges1 = [(0, 1), (0, 4), (4, 1), (4, 3), (3, 2), (1, 2), (1, 3)]

num_nodes2 = 9
edges2 = [(0, 1), (0, 3), (1, 2), (2, 3), (4, 5), (4, 6), (5, 6), (7, 8)]


class Graph:
    def __init__(self, num_nodes: int, edges: list):
        self.num_nodes = num_nodes
        self.data: list = [[] for x in range(num_nodes)]
        for n1, n2 in edges:
            # create bidirectional edge list - for each node creates a list of nodes
            # it is attached to (using (n1,n2) from each tuple)
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def __repr__(self):
        # use \n to join together multiple list entries with a line break between each one
        return "\n".join(
            ["{}: {}".format(n, neighbours) for n, neighbours in enumerate(self.data)]
        )

    def __str__(self) -> str:
        return self.__repr__()

    # add new edges
    def add_edge(self, new_edge: tuple):
        if len(new_edge) != 2:
            raise ValueError("Node must be tuple of 2")
        # unpack tuple
        n1, n2 = new_edge

        if n1 < 0 or n2 < 0:
            # Check that the node IDs are within the valid range
            raise ValueError("Node IDs must be more than 0")

        # Update num_nodes if necessary
        if n1 >= self.num_nodes or n2 >= self.num_nodes:
            self.num_nodes = max(n1, n2) + 1  # Update the number of nodes
            self.data.extend([] for _ in range((self.num_nodes) - len(self.data)))

        self.data[n1].append(n2)
        self.data[n2].append(n1)

    # remove edges
    def remove_edge(self, bin_node: tuple):
        n1, n2 = bin_node
        self.data[n1].remove(n2)
        self.data[n2].remove(n1)


graph1 = Graph(num_nodes1, edges1)
graph2 = Graph(num_nodes2, edges2)

# use print functions to show how adding and removing work with this dataset
# graph1.add_edge((2, 5))
# print(graph1)
# graph1.remove_edge((2, 5))
# print(graph1)


"""
Represent a graph as an adjacency matrix in Python
"""


class AdjMatrix:
    def __init__(self, num_nodes: int, edges: list):
        self.num_nodes = num_nodes
        # create table n*n of 0s, where n is number of nodes
        self.data: list = [[0 for x in range(num_nodes)] for x in range(num_nodes)]
        for n1, n2 in edges:
            self.data[n1][n2] = 1
            self.data[n2][n1] = 1

    # represent in table form
    def __repr__(self):
        return "\n".join(
            ["{}: {}".format(n, edges) for n, edges in enumerate(self.data)]
        )


# matrix1 = AdjMatrix(num_nodes, edges)
# print(matrix1)

"""
Implement breadth-first search given a source node in a graph using Python.
Complexity is O(m+n) - where m and n are number of edges and number of nodes

BFS pseudocode (Wikipedia):

    1  procedure BFS(G, root) is
    2      let Q be a queue
    3      label root as discovered
    4      Q.enqueue(root)
    5      while Q is not empty do
    6          v := Q.dequeue()
    7          if v is the goal then
    8              return v
    9          for all edges from v to w in G.adjacentEdges(v) do
    10              if w is not labeled as discovered then
    11                  label w as discovered
    12                  Q.enqueue(w)
"""


def bfs(graph_input: Graph, root):
    # create a queue list
    queue = []
    # mark each node as undiscovered
    discovered = [False] * len(graph_input.data)
    # create list of distance of each node from root
    distance = [None] * len(graph_input.data)
    # when discovered, mark that list entry with the root number/value
    discovered[root] = root
    discovery_order = [root]
    # create list of parents for each node
    parent = [None] * len(graph_input.data)
    # then add the node (in this case the root) to the queue
    queue.append(root)
    # the root is distance 0 from itself
    distance[root] = 0

    while len(queue) > 0:
        # take value from front of queue
        current = queue.pop(0)

        # go through all the entries in list self.data for current node
        for node in graph_input.data[current]:
            if discovered[node] is False:
                # its distance is 1+distance of parent node from root
                # breadth first search always goes to closest nodes first so as long as
                # this was previously undiscovered, it is correct
                distance[node] = 1 + distance[current]
                # add it to discovery order list
                discovery_order.append(node)
                discovered[node], parent[node] = node, current
                # add this node to the queue to examine its connected nodes too
                queue.append(node)

    return discovered, distance, parent, discovery_order


print(bfs(graph1, 1))


"""
Question: Write a program to check if all the nodes in a graph are connected
"""


# check if any connections are left undiscovered i.e. not connected
def check_connection(graph_input: Graph):
    discovered_nodes = bfs(graph_input, 0)[0]
    for x in discovered_nodes:
        if x is False:
            return False

    return True


# so for graph1, will be true, for graph2 would be false as (7,8) only
# connected to each other

"""
To find number of connected components, commence BFS, then repeat if any undiscovered
nodes. Continue until all nodes discovered
"""


"""
Question: Implement depth first search from a given node in a graph using Python.

DFS pseudocode (Wikipedia):
procedure DFS_iterative(G, v) is
    let S be a stack
    S.push(v)
    while S is not empty do
        v = S.pop()
        if v is not labeled as discovered then
            label v as discovered
            for all edges from v to w in G.adjacentEdges(v) do 
                S.push(w)
"""


# code is mostly same as for bfs but with stack instead of queue
def dfs(graph_input: Graph, root):
    # create a stack list (last in first out)
    stack = []
    stack.append(root)

    discovered = [False] * len(graph_input.data)
    discovered[root] = root
    distance = [None] * len(graph_input.data)
    discovery_order = [root]
    parent = [None] * len(graph_input.data)
    distance[root] = 0

    while len(stack) > 0:
        # take value from end of stack
        current = stack.pop()

        for node in graph_input.data[current]:
            if discovered[node] is False:
                distance[node] = 1 + distance[current]
                discovery_order.append(node)
                discovered[node], parent[node] = node, current
                stack.append(node)

    return discovered, distance, parent, discovery_order


print(dfs(graph1, 1))

"""
DFS is not great for finding shortest distance, use BFS instead for this
"""

"""
Question: Write a function to detect a cycle in a graph
"""
