from queue import PriorityQueue


def GBFS(graph, heu,  src, des):
    frontier = PriorityQueue()
    exp = []
    path = []
    path.append( src)
    frontier.put((heu[ src], path))
    while frontier and not frontier.empty():
        heuristic, node = frontier.get()
        cur = node[-1]
        if cur not in exp:
            if cur == des:
                return exp, node
            exp.append(cur)
            for fr in range(len(graph[cur])):
                if fr not in exp and graph[cur][fr] != 0:
                    totalHeu = heu[fr]
                    path = node.copy()
                    path.append(fr)
                    frontier.put((totalHeu, path))
    return exp, None
