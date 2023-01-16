class Solution:
    def commonChars(self, words: List[str]) -> List[str]:        
        firstFreq = Counter(words[0])
        commonChar = []
        
        for i in range(1,len(words)):
            firstFreq = firstFreq & Counter(words[i])
            
        
        for c, v in firstFreq.items():
            for i in range(v):
                commonChar.append(c)
                
        return commonChar
                
                
                
                