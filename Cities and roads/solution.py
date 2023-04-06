n = int(input())
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

count = 0
for r in range(len(graph)):
    for c in range(len(graph[r])):
        if graph[r][c] == 1:
            count += 1

print(count // 2)




