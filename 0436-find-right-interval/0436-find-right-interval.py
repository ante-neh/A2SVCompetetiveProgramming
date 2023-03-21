class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        rightInterval = [-1] * len(intervals)
        temp = sorted(intervals)
        
        for index, interval in enumerate(intervals):
            left, right = -1, len(intervals)
            while left + 1 < right:
                mid = left + (right - left) // 2
                
                if temp[mid][0] < interval[1]:
                    left = mid
                    
                else:
                    right = mid
                    
            if right != len(intervals):
                rightInterval[index] = intervals.index(temp[right])
            
                
        return rightInterval