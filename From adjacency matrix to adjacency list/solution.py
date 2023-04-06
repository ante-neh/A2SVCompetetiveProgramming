from collections import defaultdict
n = int(input())
matrix = []
graph = defaultdict(list)
for _ in range(n):
    matrix.append(list(map(int, input().split())))

for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        if matrix[r][c] == 1:
            graph[r + 1].append(c + 1)

for i in graph:
    print(len(graph[i]), *graph[i])