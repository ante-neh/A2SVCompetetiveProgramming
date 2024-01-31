class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numsGreater = [-1] * len(nums2)
        stack = []
        indexPair = []
        ans = []
        
        for num in nums1:
            indexPair.append(nums2.index(num))

        for index, num in enumerate(nums2):
            while stack and stack[-1][0] < num:
                val, i = stack.pop()
                numsGreater[i] = num

            stack.append([num, index])

        for index in indexPair:
            ans.append(numsGreater[index])

        return ans


        