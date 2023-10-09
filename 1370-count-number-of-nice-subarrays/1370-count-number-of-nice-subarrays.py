class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        sumDifferencePair = defaultdict(int)
        sumDifferencePair[0] = 1
        count = 0
        curSum = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        print(nums)
        for num in nums:
            curSum += num

            if curSum - k in sumDifferencePair:
                count += sumDifferencePair[curSum - k]

            sumDifferencePair[curSum] += 1

        return count

        

        