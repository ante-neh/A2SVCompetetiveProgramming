n, m = map(int, input().split())
grid = []
for i in range(n):
    row = input()
    grid.append(row)

def check(row, col,val):
    for c in range(len(grid[0])):
        if grid[row][c] == val and c != col:
            return True

    for r in range(len(grid)):
        if grid[r][col] == val and r != row:
            return True

    return False

ans = ""

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if not check(r, c, grid[r][c]):
            ans += grid[r][c]

print(ans)