class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        namesToHeights = {}
        
        for i in range(len(names)):
            namesToHeights[heights[i]] = names[i]
            
        for i in range(len(heights)):
            for j in range(len(heights) - i - 1):
                if heights[j] <= heights[j + 1]:
                    heights[j], heights[j + 1] = heights[j + 1], heights[j]
                    
        for i in range(len(heights)):
            names[i] = namesToHeights[heights[i]]
            
        return names