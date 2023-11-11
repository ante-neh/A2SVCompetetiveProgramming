class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False 

        flip, stack = [], []
        
        for i, c in enumerate(s):
            if locked[i] == '0':
                flip.append(i)

            else:
                if c == '(':
                    stack.append(i)

                else:
                    if stack:
                        stack.pop()
                    elif flip:
                        flip.pop()
                    else:
                        return False

        while flip and stack:
            if stack[-1] > flip[-1]:
                return False

            stack.pop()
            flip.pop()

        return len(stack) == 0

