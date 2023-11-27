class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # helper function to get number of pairs that have sum less than maxSum
        def getAvailablePairs(maxSum: int) -> int:
            availablePairs = 0
            for i in range(len(nums1)):
                it = bisect_right(nums2, maxSum - nums1[i])
                availablePairs += it
            return availablePairs
        
        # calculate the sum of the k-th pair with binary search
        NUM_MAX = 2000000000
        lo, hi = -NUM_MAX, NUM_MAX
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if getAvailablePairs(mi) >= k:
                hi = mi
            else:
                lo = mi + 1
        
        # calculate the number of pairs with sum exactly equal to lo
        maxSumPairs = k - getAvailablePairs(lo - 1)
        
        # construct the final answer by iterating pairs with sum not greater than lo
        ans = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] + nums2[j] < lo:
                    ans.append([nums1[i], nums2[j]])
                elif nums1[i] + nums2[j] == lo and maxSumPairs > 0:
                    ans.append([nums1[i], nums2[j]])
                    maxSumPairs -= 1
                else:
                    break
        return ans
