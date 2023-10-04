class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        k = len(words) * len(words[0])
        wordLength = len(words[0])
        result = []
        left = 0
        sCount = defaultdict(int)
        wordsCount = defaultdict(int)

        for word in words:
            for c in word:
                wordsCount[c] += 1

        for right in range(len(s)):
            sCount[s[right]] += 1

            if right - left + 1 == k:
                temp = []
                if sCount == wordsCount:
                    for i in range(left, left + k, wordLength):
                        temp.append(s[i:i + wordLength])
                    

                    if Counter(words) == Counter(temp):
                        result.append(left)

                sCount[s[left]] -= 1

                if sCount[s[left]] == 0:
                    sCount.pop(s[left])
                
                left += 1

        return result

