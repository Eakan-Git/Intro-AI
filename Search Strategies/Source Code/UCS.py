from queue import PriorityQueue

def UCS(graph, src, des):
    frontier = PriorityQueue()
    exp = []
    path = []
    path.append(src)
    frontier.put((0, path))
    while frontier and not frontier.empty():
        cost, node = frontier.get()
        cur = node[-1]
        if cur not in exp:
            exp.append(cur)
            if cur == des:
                return exp, node
            for i in range(len(graph[cur])):
                if i not in exp and graph[cur][i] != 0:
                    totalCost = cost + graph[cur][i]
                    path = node.copy()
                    path.append(i)
                    frontier.put((totalCost, path))
    return exp, None
