import numpy as np
from itertools import chain
from BFS import *
from DFS import DFS
from UCS import *
from IDS import IDS
from GBFS import *
from AStar import *
def checkIsolated(graph, node):
    for i in range(len(graph[node])):
        if graph[node][i] != 0:
            return False
    return True

def main():
    with open('input.txt', 'r') as f:
        readLines = f.readlines()
        lines = [line[:-1] for line in readLines if line[-1] == '\n']
        lines.append(readLines[-1])
        f.close()

    n = int(lines[0])
    line2 = list(lines[1].split(" "))
    src = int(line2[0])
    des = int(line2[1])
    alg = int(line2[2])

    graph = []
    for i in range(n):
        graph.append(list(lines[i+2].split(" ")))

    graph = [list(map(int, i)) for i in graph]
    heu = list(lines[-1].split(" "))
    heu = list(map(int, heu))
    #print(n, src, des)
    #print(graph)
    #print(heu)

    if checkIsolated(graph, src):
        return None, None

    if alg == 0:
        print("Find path from ", src, " to ", des, "using BFS:")
        exp, res = BFS(graph, src, des)
    elif alg == 1:
        print("Find path from ", src, " to ", des, "using DFS:")
        exp, res = DFS(graph, src, des)
    elif alg == 2:
        print("Find path from ", src, " to ", des, "using UCS:")
        exp, res = UCS(graph, src, des)
    elif alg == 3:
        print("Find path from ", src, " to ", des, "using IDS:")
        exp, res = IDS(graph, src, des)
        #for outputting:
        exp = list(chain.from_iterable(exp))
    elif alg == 4:
        print("Find path from ", src, " to ", des, "using GBFS:")
        exp, res = GBFS(graph, heu, src, des)
    elif alg == 5:
        print("Find path from ", src, " to ", des, "using AStar:")
        exp, res = AStar(graph, heu, src, des)
    print("Expanded nodes: ", exp)
    print("Path returned: ", res)

    expStr = ' '.join(map(str, exp))
    if res is not None:
        pathStr = ' '.join(map(str, res))
    else:
        pathStr = 'No path exists.'
    with open('output.txt', 'w') as f:
        f.write(expStr+'\n')
        f.write(pathStr)
        f.close()
main()