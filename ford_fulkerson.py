class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    def path_exist(self, s, t, parent):
        visited = [False] * len(self.graph)
        queue = list()
        queue.append(s)
        visited[s] = True
        while queue:
            currentNode = queue.pop(0)
            for newNode, capacity in enumerate(self.graph[currentNode]):
                if visited[newNode] is False and capacity > 0:
                    queue.append(newNode)
                    visited[newNode] = True
                    parent[newNode] = currentNode
        return True if visited[t] else False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * len(self.graph)
        max_flow = 0
        while self.path_exist(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                min_path_capacity = self.graph[parent[s]][s]
                path_flow = min(path_flow, min_path_capacity)
                s = parent[s]
            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow

if __name__ == '__main__':
    graph = [[0, 8, 0, 0, 3, 0],
             [0, 0, 9, 0, 0, 0],
             [0, 0, 0, 0, 7, 2],
             [0, 0, 0, 0, 0, 5],
             [0, 0, 7, 4, 0, 0],
             [0, 0, 0, 0, 0, 0]]
    g = Graph(graph)
    source = 0
    sink = 5
    print(g.ford_fulkerson(source, sink))