class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nextGreater = [-1] * (len(nums))
        stack = []
        
        for index, num in enumerate(2 * nums):
            while stack and stack[-1][0] < num:
                val, ind = stack.pop()
                nextGreater[ind] = num
                
            if index < len(nums):
                stack.append([num, index])
                
        return nextGreater