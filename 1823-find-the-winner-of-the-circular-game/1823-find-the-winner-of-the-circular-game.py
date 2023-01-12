class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [item for item in range(1,n+1)]
        index, operation = 0, k - 1
        winner = None
        
        while nums:
            rem = (index + operation) % len(nums)
            winner = nums.pop(rem)
            index = rem
            
        return winner
        
        