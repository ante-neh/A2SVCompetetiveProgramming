class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = [] 
        def isValid(mid):
            count = 0
            for num in nums1:
                count += bisect.bisect_right(nums2, mid - num)
            
            return [count >= k, count]

        left, right = nums1[0] + nums2[0] - 1, nums1[-1] + nums2[-1] + 1

        while left + 1 < right:
            mid = left + (right - left) // 2
            if isValid(mid)[0]:
                right = mid

            else:
                left = mid 

        maxNumberOfPairs = k - isValid(left)[1]

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] + nums2[j] < left + 1:
                    result.append([nums1[i], nums2[j]])

                elif nums1[i] + nums2[j] == left + 1 and maxNumberOfPairs > 0:
                    result.append([nums1[i], nums2[j]])
                    maxNumberOfPairs -= 1
                else:
                    break

                
        return result
