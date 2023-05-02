class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        n, m = len(board), len(board[0])
        def get_next_state(state):
            state = list(state)
            index = state.index(0)
            i, j = divmod(index, m)
            next_state = []
            for x, y in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                if 0 <= x < n and 0 <= y < m:
                    new_state = state.copy()
                    new_state[index], new_state[x*m+y] = new_state[x*m+y], new_state[index]
                    new_state = tuple(new_state)
                    if new_state not in visited:
                        visited.add(new_state)
                        next_state.append(new_state)
            return next_state            
                    
        initial = []
        final = (1,2,3,4,5,0)
        for i in range(n):
            for j in range(m):
                initial.append(board[i][j])
        initial = tuple(initial)        
        queue = collections.deque([(initial, 0)])
        visited = set([initial])
        while queue:
            state, dist = queue.pop()
            if state == final: return dist
            for nstate in get_next_state(state):
                queue.appendleft((nstate, dist+1))
        return -1