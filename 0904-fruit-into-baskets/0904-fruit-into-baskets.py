class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxLen = 0
        left = 0
        fruitsCount = {}
        
        for right in range(len(fruits)):
            fruitsCount[fruits[right]] = 1 + fruitsCount.get(fruits[right], 0)
            
            while len(fruitsCount) > 2:
                fruitsCount[fruits[left]] -= 1
                if fruitsCount[fruits[left]] == 0:
                    fruitsCount.pop(fruits[left])
                    
                left += 1
                
            maxLen = max(maxLen, right - left + 1)
            
        return maxLen
                    