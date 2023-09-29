class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubsequence(word1, word2):
            p1, p2 = 0, 0
            while p1 < len(word1) and p2 < len(word2):
                if word1[p1] == word2[p2]:
                    p1 += 1
                
                p2 += 1

            return p1 == len(word1)

            
        strs.sort(key = len, reverse = True)
        for i in range(len(strs)):
            flag = True
            for j in range(len(strs)):
                if i != j and isSubsequence(strs[i], strs[j]):
                    flag = False
                    break
            if flag:
                return len(strs[i])

        return -1
