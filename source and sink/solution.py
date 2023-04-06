n = int(input())
graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

def findSourcesAndSinks(matrix):
    sources, sinks = [], []
    for r in range(len(matrix)):
        count = 0
        for c in range(len(matrix[r])):
            if matrix[r][c] == 1:
                count = 1
                break
        
        if count == 0:
            sinks.append(r + 1)

    for c in range(len(matrix[0])):
        count = 0
        for r in range(len(matrix)):
            if matrix[r][c] == 1:
                count = 1
                break
        
        if count == 0:
            sources.append(c + 1)

    return sources, sinks

sources, sinks = findSourcesAndSinks(graph)
print(len(sources), *sources)
print(len(sinks), *sinks)            