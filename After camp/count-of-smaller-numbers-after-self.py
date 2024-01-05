class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.countAfter = [0] * len(nums)
        newNum = [[index, v] for index, v in enumerate(nums)]

        def mergeSort(nums):
            if len(nums) < 2:
                return nums

            mid = len(nums) // 2
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])

            return self.merge(left, right)
            
        mergeSort(newNum)

        return self.countAfter
        
    def merge(self, nums1, nums2):
        for i in range(len(nums1)):
            count = self.binarySearch(nums2, nums1[i][1])
            self.countAfter[nums1[i][0]] += count


        merged = []
        p1, p2 = 0, 0

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1][1] <= nums2[p2][1]:
                merged.append(nums1[p1])
                p1 += 1
            
            else:
                merged.append(nums2[p2])
                p2 += 1

        merged.extend(nums1[p1:] or nums2[p2:])

        return merged

    def binarySearch(self, nums, target):
        left, right = -1, len(nums)

        while left + 1 < right:
            mid = left + (right - left) // 2

            if nums[mid][1] >= target:
                right = mid
            
            else:
                left = mid


        return left + 1
