class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0] # initialize stack with a 0 to handle the case of a single pair of parentheses
        
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                score = stack.pop()
                
                if score == 0:
                    score = 1
                elif score != 0:
                    score *= 2
                
                stack[-1] += score
                
        return stack[0]
        