class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def backtrack(ci, dist):
            if ci == len(cookies):
                self.result = min(self.result, max(dist))
                return
                
            for di in range(k):
                dist[di] += cookies[ci]
                if dist[di] < self.result:
                    backtrack(ci + 1, dist)
                dist[di] -= cookies[ci]
                
        self.result = math.inf
        backtrack(0, [0]*k)
        
        return self.result