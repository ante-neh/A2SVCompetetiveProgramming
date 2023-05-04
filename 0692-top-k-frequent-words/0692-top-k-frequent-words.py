class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordsFreq = defaultdict(int)
        result = []
        heap = []
        for word in words:
            wordsFreq[word] -= 1
            
        for item in wordsFreq.items():
            heap.append(item[::-1])
            
        heapify(heap)
        for i in range(k):
            result.append(heappop(heap)[1])
            
        return result
        