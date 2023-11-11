class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        nums = [0] * len(s)
        maxLength = 0
        left = 0
        if len(s) == 0:
            return 0

        for index, c in enumerate(s):
            if stack and s[stack[-1]] == '(' and c == ')':
                nums[stack.pop()] = 1
                nums[index] = 1

            else:
                stack.append(index)

        
        for right in range(len(nums)):
            if nums[right] == 0:
                maxLength = max(maxLength, right - left)
                left = right + 1

        
        return max(maxLength, right - left + 1)


