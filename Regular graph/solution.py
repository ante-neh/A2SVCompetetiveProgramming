n, m = map(int, input().split())
matrix = []
if m == 0:
    print('YES')
else:
    for _ in range(m):
        matrix.append(list(map(int, input().split())))
    vertexCount = {}

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            vertexCount[matrix[r][c]] = 1 + vertexCount.get(matrix[r][c], 0)


    if max(vertexCount.values()) == min(vertexCount.values()):
        print("YES")
    else:
        print("NO")