def BFS(graph, src, des):
    explored = []
    expanded = []
    queue = [[src]]
    expanded.append(src)
    if src == des:
        return expanded, [src]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in expanded:
            expanded.append(node)
        if node not in explored:
            for i in range(len(graph[node])):
                if graph[node][i] != 0:
                    newPath = list(path)
                    newPath.append(i)
                    queue.append(newPath)
                    if i == des:
                        return expanded, newPath
            explored.append(node)
    return expanded, None