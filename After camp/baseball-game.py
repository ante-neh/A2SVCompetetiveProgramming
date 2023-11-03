class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for ops in operations:
            if ops == '+':
                stack.append(stack[-1] + stack[-2])
            
            elif ops == 'C':
                stack.pop()
            
            elif ops == 'D':
                stack.append(stack[-1] * 2)

            else:
                stack.append(int(ops))

        return sum(stack)