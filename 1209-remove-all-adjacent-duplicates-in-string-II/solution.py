class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        result=""
        for char in s:
            if stack and stack[-1][0]==char:
                stack[-1][1]+=1
            else:
                stack.append([char,1])
            if stack[-1][1]==k:
                stack.pop()
        for char,count in stack:
            result+=(char*count)
        return result
    #time complexity O(n)
    #space complexity O(n)