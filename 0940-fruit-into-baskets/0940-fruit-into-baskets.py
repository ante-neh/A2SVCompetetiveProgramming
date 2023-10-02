class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruitsCount = defaultdict(int)
        left = 0
        maxFruits = 0
        curSum = 0

        
        for right in range(len(fruits)):
            fruitsCount[fruits[right]] += 1
            curSum += 1

            while len(fruitsCount) > 2:
                fruitsCount[fruits[left]] -= 1
                if fruitsCount[fruits[left]] == 0:
                    fruitsCount.pop(fruits[left])
                
                left += 1
                curSum -= 1

            maxFruits = max(maxFruits, curSum)

        return maxFruits  