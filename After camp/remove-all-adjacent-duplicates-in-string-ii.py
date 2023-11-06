class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = deque()

        for c in s:
            if stack and stack[-1][0] == c:
                stack.append([c, stack[-1][1] + 1])
                
            else:
                stack.append([c, 1])
                
            count = k
            while stack and stack[-1][1] == k :
                stack.pop()
                k -= 1

            k = count

        length = len(stack)
        for i in range(length):
            c, count = stack.popleft()
            stack.append(c)

        return "".join(stack)
