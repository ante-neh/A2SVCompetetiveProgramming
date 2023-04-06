from collections import defaultdict
n = int(input())
k = int(input())
graph = defaultdict(list)

for _ in range(k):
    operations = list(map(int, input().split()))
    if operations[0] == 1:
        graph[operations[1]].append(operations[2])
        graph[operations[2]].append(operations[1])

    if operations[0] == 2:
        print(*graph[operations[1]])
