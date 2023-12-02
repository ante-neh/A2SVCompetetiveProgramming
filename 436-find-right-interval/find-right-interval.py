class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:            
        startToIndex = defaultdict(int)
        i = 0
        for interval in intervals:
            startToIndex[interval[0]] = i 
            i += 1

        result = [-1] * len(intervals)
        intervals.sort(key = lambda x:x[0])

        for interval in intervals:
            left, right = 0, len(intervals)
            while left + 1 < right:
                mid = left + (right - left) // 2
                
                if intervals[mid][0] >= interval[-1]:
                    result[startToIndex[interval[0]]] = startToIndex[intervals[mid][0]]
                    right = mid

                elif intervals[mid][0] > interval[-1]:
                    right = mid

                else:
                    left = mid

            if interval[-1] <= intervals[left][0]:
                result[startToIndex[interval[0]]] = startToIndex[intervals[left][0]]

        return result 
