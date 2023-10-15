class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        currentEvenSum = 0
        result = []

        for num in nums:
            if num % 2 == 0:
                currentEvenSum += num

        for val, index in queries:
            if val % 2 == 0 and nums[index] % 2 == 0:
                currentEvenSum += val
            
            elif val % 2 == 1 and nums[index] % 2 == 1:
                currentEvenSum += (val + nums[index])


            elif val % 2 == 1 and nums[index] % 2 == 0:
                currentEvenSum -= nums[index]
                
            nums[index] += val
            result.append(currentEvenSum)

        return result

        