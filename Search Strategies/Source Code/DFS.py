def findPath(graph, cur, des, seen, exp):
	exp.append(cur)
	if cur == des:
		return [cur]
	for fr in range(0, len(graph[cur])):
		if graph[cur][fr] != 0:
			if fr not in seen:
				seen.add(fr)
				path = findPath(graph, fr, des, seen, exp)
				if path is not None:
					path.insert(0, cur)
					return path
	return None

def DFS(graph, src, des):
	exp = []
	seen = set()
	if src < 0 or des > len(graph):
		return False
	seen.add(src)
	res = findPath(graph, src, des, seen, exp)
	return exp, res
