class Solution:
    def largestGoodInteger(self, num: str) -> str:
        left = 0
        maxNumber = float("-inf")
        result = ""
        counter = defaultdict(int)

        for right in range(len(num)):
            counter[num[right]] += 1

            if right - left + 1 == 3:
                if int(num[left:right + 1]) > maxNumber and len(counter) == 1:
                    result = num[left:right + 1]
                    maxNumber = int(num[left:right + 1])
                
                counter[num[left]] -= 1
                if counter[num[left]] == 0:
                    del counter[num[left]]
                    
                left += 1

        return result
