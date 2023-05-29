class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        arr = [0 for i in range(n)]
        
        
        if len(cost)==1:
            return 0
        
        arr[0] = cost[0]
        arr[1] = cost[1]
        
        for i in range(2,n):
            arr[i] = cost[i] + min(arr[i-1],arr[i-2])
            
        return min(arr[n-1],arr[n-2])