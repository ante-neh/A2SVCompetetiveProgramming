class Solution:
    def __init__(self, nums, k):
        self.k = k
        self.nums = nums

    def mergeSort(self, nums):
        if len(nums) < 2:
            return nums
        
        mid = len(nums) // 2

        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])

        return self.merge(left, right)
    
    def merge(self, nums1, nums2):
        p1, p2 = 0, 0
        merged = []
        while p1 < len(nums1) and p2 < len(nums2):
            if self.nums[nums1[p1]] - self.nums[nums2[p2]] > self.k:
                p2 += 1
            elif self.nums[nums2[p2]] - self.nums[nums1[p1]] > self.k:
                p1 += 1

            else:
                break

        while p1 < len(nums1) and p2 < len(nums2):
            if self.nums[nums1[p1]] < self.nums[nums2[p2]]:
                merged.append(nums1[p1])
                p1 += 1
            
            else:
                merged.append(nums2[p2])
                p2 += 1

        merged.extend(nums1[p1:] or nums2[p2:])

        return merged 
    

n, k = map(int, input().split())
nums = list(map(int, input().split()))
indecies = [i for i in range(len(nums))]
obj = Solution(nums, k)
result = obj.mergeSort(indecies)
result.sort()
result = [i + 1 for i in result]

print(*result)