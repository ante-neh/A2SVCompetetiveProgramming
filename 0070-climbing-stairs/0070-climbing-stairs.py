class Solution:
    def __init__(self):
        self.memo = {1:1, 2:2}
        
    def climbStairs(self, n: int) -> int:        
        if not n in self.memo:
            self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return self.memo[n]