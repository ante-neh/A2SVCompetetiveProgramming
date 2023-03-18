class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # do this with a monotonic stack?
        stack = []
        seen = set()
        
        # O(n) time preprocessing
        last = {c:i for i,c in enumerate(s)}
        
        # O(n) time
        for i, c in enumerate(s):
            if c not in seen:
                # 1. if stack has stuff inside
                # 2. check if the element happens later and is bigger than c,
                # if so, remove it because we can get it later.
                while stack and c < stack[-1] and last[stack[-1]] > i:
                    seen.remove(stack.pop())
                seen.add(c)
                stack.append(c)
        return ''.join(stack)