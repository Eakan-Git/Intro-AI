from queue import PriorityQueue


def AStar(graph, heu, src, des):
    exp = []
    path = []
    parents = {}
    frontier = PriorityQueue()
    frontier.put((0, src, None))
    while frontier and not frontier.empty():
        cost, node, p = frontier.get()
        if node not in exp:
            exp.append(node)
            parents[node] = p
            if node is des:
                while parents[node] is not None:
                    path.append(node)
                    node = parents[node]
                path.append(src)
                return exp, path[::-1]
            for child in range(len(graph[node])):
                if child not in exp and graph[node][child] != 0:
                    gChild = cost + graph[node][child]
                    hChild = heu[child]
                    fChild = gChild + hChild - heu[node]
                    frontier.put((fChild, child, node))
    return exp, None
