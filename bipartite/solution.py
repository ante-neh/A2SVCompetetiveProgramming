from collections import defaultdict
def isBipartite(graph, n):
    color = [0] * n
    for u in range(1, n + 1):
        if color[u - 1] == 0:
            color[u - 1] = 1

        for v in graph[u]:
            if color[v - 1] == color[u - 1]:
                return False
            color[v -1] = -1 * color[u - 1]
                
    return True
        
while True:
    n = int(input())
    if n == 0:
        break

    l = int(input())
    graph = defaultdict(list)
    for _ in range(l):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    if isBipartite(graph, n):
        print("BICOLOURABLE.")
    else:
        print("NOT BICOLOURABLE.")

