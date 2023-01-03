class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        modifiedString = []
        spaceIndex = 0
        
        for stringIndex in range(len(s)):
            if spaceIndex < len(spaces) and stringIndex == spaces[spaceIndex]:
                modifiedString.append(" ")
                spaceIndex += 1
                
            modifiedString.append(s[stringIndex])
            
        return "".join(modifiedString)
    
                
                
                
            