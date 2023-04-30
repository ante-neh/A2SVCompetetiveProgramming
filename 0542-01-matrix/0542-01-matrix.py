class Solution:
	def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
		m = len(mat)
		n = len(mat[0])
		directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
		queue = collections.deque()
		toChange = set()
		for i in range(m):
			for j in range(n):
				if mat[i][j] == 0:
					queue.append((i, j, 0))
				else:
					toChange.add((i, j))
		while queue:
			x, y, d = queue.popleft()
			for direction in directions:
				nx = x + direction[0]
				ny = y + direction[1]
				if 0 <= nx < m and 0 <= ny < n and mat[nx][ny] != 0 and (nx, ny) in toChange:
					mat[nx][ny] = d + 1
					queue.append((nx, ny, d + 1))
					toChange.remove((nx, ny))
		return mat