class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        leftMin = float("inf")

        for num in nums:
            while stack and stack[-1][0] <= num:
                stack.pop()

            if stack and num > stack[-1][1]:
                return True

            stack.append([num, leftMin])
            leftMin = min(leftMin, num)

        return False 
