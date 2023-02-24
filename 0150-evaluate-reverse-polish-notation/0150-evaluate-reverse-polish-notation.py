class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                nums1 = stack.pop()
                nums2 = stack.pop()
                
                if token == '+':
                    stack.append(nums1 + nums2)
                elif token == '-':
                    stack.append(nums2 - nums1)
                elif token == '*':
                    stack.append(nums1 * nums2)
                else:
                    stack.append(int(nums2/nums1))
                    
            else:
                stack.append(int(token))
                
        return stack[-1]