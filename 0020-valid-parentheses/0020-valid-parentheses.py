class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen={')':'(','}':'{',']':'['}
        stack=[]
        for char in s:
            if char in closeToOpen and stack and closeToOpen[char]==stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return len(stack)==0
                