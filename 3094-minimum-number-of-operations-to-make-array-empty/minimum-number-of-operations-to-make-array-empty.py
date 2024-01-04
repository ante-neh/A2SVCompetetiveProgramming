class Solution:
    def minOperations(self, nums: List[int]) -> int:
        numFreq = Counter(nums)
        minimumNumberOfOperations = 0

        for num, count in numFreq.items():
            if count == 1:
                return -1

            minimumNumberOfOperations += math.ceil(count / 3)

        return minimumNumberOfOperations