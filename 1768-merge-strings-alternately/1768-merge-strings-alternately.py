class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        n = 0
        
        while n < len(word1) and n < len(word2):
            merged += word1[n]
            merged += word2[n]
            n += 1
            
        while n < len(word1):
            merged += word1[n]
            n += 1
            
        while n < len(word2):
            merged += word2[n]
            n += 1
            
        return merged