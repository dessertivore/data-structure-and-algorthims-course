"""
Creat graph class for graphs with weighted edges and possibility of direction
"""
num_nodes5 = 9
edges5 = [
    (0, 1, 3),
    (0, 3, 2),
    (0, 8, 4),
    (1, 7, 4),
    (2, 7, 2),
    (2, 3, 6),
    (2, 5, 1),
    (3, 4, 1),
    (4, 8, 8),
    (5, 6, 8),
]

num_nodes6 = 5
edges6 = [(0, 1), (1, 2), (2, 3), (2, 4), (4, 2), (3, 0)]

num_nodes7 = 6
edges7 = [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)]


# class definition from tutor
class WeightedEdgeGraph:
    def __init__(self, num_nodes: int, edges: list, directed=False, weighted=False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.weighted = weighted
        self.data: list = [[] for _ in range(num_nodes)]

        self.weight: list = [
            [] for _ in range(num_nodes)
        ]  # save weight of edge between each corresponding node
        self.weighted = len(edges) > 0 and len(edges[0]) == 3

        for edge in edges:
            node1, node2, weight = edge
            self.data[node1].append(node2)
            if self.weighted:  # add weight if weighted
                self.weight[node1].append([node2, weight])
            if not directed:  # store both directions if not directed
                self.data[node2].append(node1)
                if self.weighted:
                    self.weight[node2].append([node1, weight])

    def __repr__(self):
        result = ""
        for i in range(len(self.data)):
            pairs = list(zip(self.data[i], self.weight[i] if self.weighted else []))
            result += "{}: {}\n".format(i, pairs)
        return result

    def __str__(self):
        return repr(self)


g7 = WeightedEdgeGraph(num_nodes7, edges7, directed=False, weighted=True)
# print(g7)
# print(g7.weight)
