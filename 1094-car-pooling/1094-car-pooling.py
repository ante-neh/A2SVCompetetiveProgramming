class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxLen = 0
        
        for trip in trips:
            maxLen = max(maxLen, trip[2])
            
        capacityArray = [0] * (maxLen + 1)

        for trip in trips:
            capacityArray[trip[1]] += trip[0]
            capacityArray[trip[2]] -= trip[0]
            
        for i in range(1, len(capacityArray)):
            capacityArray[i] += capacityArray[i - 1]
            
        for i in range(len(capacityArray)):
            if capacityArray[i] > capacity:
                return False
            
        return True