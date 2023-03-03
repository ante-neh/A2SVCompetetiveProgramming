class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        wordsFreq = []
        answer = []
        queriesFreq = []
        
        #buliding array which stores frequency of the smallest character in each strings of words
        
        for word in words:
            count = 0
            minC = min(word)
            for c in word:
                if c == minC:
                    count += 1
            wordsFreq.append(count)
        
        #sort the array inorder to impeliment binary search over it
        wordsFreq.sort()
        
        #buliding array which stores frequency of the smallest character in each strings of queries
        for query in queries:
            minC = min(query)
            count = 0
            
            for c in query:
                if c == minC:
                    count += 1
            queriesFreq.append(count)
            
        
        #finding the positions of each values in queriesFreq array over wordsFreqarray
        for num in queriesFreq:
            left, right = -1, len(wordsFreq)
            
            while left + 1 < right:
                mid = left + (right - left) // 2
                
                if wordsFreq[mid] <= num:
                    left = mid
                else:
                    right = mid
                    
            answer.append(len(wordsFreq) - right)
            
            
        return answer