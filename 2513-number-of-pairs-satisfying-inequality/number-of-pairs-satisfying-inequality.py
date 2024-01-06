class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        self.numberOfPairs = 0
        self.diff = diff
        for i in range(len(nums1)):
            nums1[i] -= nums2[i]

        self.mergeSort(nums1)
        return self.numberOfPairs

    def mergeSort(self, nums):
        if len(nums) < 2:
            return nums
        
        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])

        return self.merge(left, right)
    
    def merge(self, nums1, nums2):
        p1, p2 = 0, 0
        result = []
        for num in nums1:
            self.numberOfPairs += len(nums2) - bisect_left(nums2, num - self.diff)
        
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                result.append(nums1[p1])
                p1 += 1
            
            else:
                result.append(nums2[p2])
                p2 += 1
                
        result.extend(nums1[p1:] or nums2[p2:])

        return result