class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if citations[-1] == 0:
            return 0
        if len(citations) <= citations[0]:
            return len(citations)
        
        n = len(citations)
        left, right = -1, n
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            
            if n - mid - 1 >= citations[mid]:
                left = mid
                
            else :
                right = mid
                
        return n - right