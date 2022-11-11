def prim(n, graph, selected_node, no_edge):
    selected_node[0] = True
    res = list()
    while (no_edge < n - 1):
        minimum = float("Inf")
        a = 0
        b = 0
        for i in range(n):
            if selected_node[i]:
                for j in range(n):
                    if ((not selected_node[j]) and graph[i][j]):
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            a = i
                            b = j
        res.append(str(a) + "-" + str(b) + " -> " + str(graph[a][b]))
        selected_node[b] = True
        no_edge += 1
    return res

if __name__ == '__main__':
    n = 5
    graph = [[0, 19, 5, 0, 0],
             [19, 0, 5, 9, 2],
             [5, 5, 0, 1, 6],
             [0, 9, 1, 0, 1],
             [0, 2, 6, 1, 0]]
    selected_node = [0, 0, 0, 0, 0]
    no_edge = 0
    res = list()
    res = prim(n, graph, selected_node, no_edge)
    for i in res:
        print(i)