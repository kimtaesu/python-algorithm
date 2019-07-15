from collections import defaultdict


# This class represents a directed graph using adjacency list representation
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def scc(self):
        identified = set()
        stack = []
        index = {}
        boundaries = []

        def dfs(v):
            index[v] = len(stack)
            stack.append(v)
            boundaries.append(index[v])

            for w in self.graph[v]:
                if w not in index:
                    # For Python >= 3.3, replace with "yield from dfs(w)"
                    for scc in dfs(w):
                        yield scc
                elif w not in identified:
                    while index[w] < boundaries[-1]:
                        boundaries.pop()

            if boundaries[-1] == index[v]:
                boundaries.pop()
                scc = set(stack[index[v]:])
                del stack[index[v]:]
                identified.update(scc)
                yield scc

        for v in range(self.V):
            if v not in index:
                # For Python >= 3.3, replace with "yield from dfs(v)"
                for scc in dfs(v):
                    yield scc


# Create a graph given in the above diagram
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)

for g in g.scc():
    print(g)
