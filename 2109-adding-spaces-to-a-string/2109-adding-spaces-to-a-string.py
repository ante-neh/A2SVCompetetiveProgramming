class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        modifiedString = []
        j = 0
        
        for i in range(len(s)):
            if j < len(spaces) and i == spaces[j]:
                modifiedString.append(" ")
                modifiedString.append(s[i])
                j += 1
                
            else:
                modifiedString.append(s[i])
                
        return "".join(modifiedString)
    
                
                
                
            