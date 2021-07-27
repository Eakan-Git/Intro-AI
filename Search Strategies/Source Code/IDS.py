MAX = 50

def DLS(graph, path, des, exp, depth):
    node = path[-1]
    if node == des:
        return path

    if depth <= 0:
        return None

    for child in range(len(graph[node])):
        if graph[node][child] != 0:
            if child not in path:
            	exp.append(child)
            	newPath = path.copy()
            	newPath.append(child)
            	next_path = DLS(graph, newPath, des, exp, depth - 1)
            	if next_path is not None:
            		return next_path
def IDS(graph, src, des):
    expArr = []
    exp = []
    for i in range(MAX):
        exp.clear()
        exp.append(src)
        path = DLS(graph, [src], des, exp, i)
        if exp not in expArr:
            expArr.append(exp.copy())
        if path is None:
            continue
        return expArr, path
    return expArr, None