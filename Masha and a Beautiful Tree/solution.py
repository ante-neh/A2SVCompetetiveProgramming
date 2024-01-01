from collections import defaultdict
import math
class Solution:
    def __init__(self):
        self.count = 0

    def mergeSort(self,nums):
        if len(nums) < 2:
            return nums
        
        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])

        return self.merge(left, right)
    
    def merge(self, nums1, nums2):
        if nums1[-1] > nums2[0]:
            self.count += 1
            return nums2 + nums1
        
        return nums1 + nums2



t = int(input())
for _ in range(t):
    m = int(input())
    nums = list(map(int, input().split()))
    numsFreq = defaultdict(int)
    for num in nums:
        numsFreq[num] += 1 
    
    if max(nums) > m or min(nums) < 1:
        print(-1)
    else:
        newObj = Solution()
        result = newObj.mergeSort(nums)
        count = newObj.count

        for i in range(1, len(result)):
            if result[i] <= result[i - 1]:
                count = -1

        print(count)