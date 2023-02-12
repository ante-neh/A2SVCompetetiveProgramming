class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxWords = 0
        
        for sentence in sentences:
            sentence = sentence.split(" ")
            maxWords = max(maxWords, len(sentence))
            
        return maxWords