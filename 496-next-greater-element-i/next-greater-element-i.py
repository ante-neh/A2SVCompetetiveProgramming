class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numsIndex = {}
        result = [-1] * len(nums1)
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                val = stack.pop()
                numsIndex[val] = num

            stack.append(num)
        
        for index, num in enumerate(nums1):
            if num in numsIndex:
                result[index] = numsIndex[num]

        return result


        