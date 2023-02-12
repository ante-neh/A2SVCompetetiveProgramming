class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxVal = max(candies)
        result = []
        
        for candy in candies:
            if candy + extraCandies >= maxVal:
                result.append(True)
            else:
                result.append(False)
                
        return result