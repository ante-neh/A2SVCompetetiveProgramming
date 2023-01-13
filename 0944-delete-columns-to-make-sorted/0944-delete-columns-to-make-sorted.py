class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for c in range(len(strs[0])):
            vertical = []
            for r in range(len(strs)):
                vertical.append(strs[r][c])
                
            if vertical != sorted(vertical):
                count += 1
        
        return count