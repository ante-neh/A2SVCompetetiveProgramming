class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = ''
        l = 0
        r = 0
        while l < len(word1) and r < len(word2):
            if word1[l:] >= word2[r:]:
                merge = merge + word1[l]
                l += 1
            else:
                merge = merge + word2[r]
                r += 1
        while l < len(word1):
            merge = merge + word1[l]
            l += 1
        while r < len(word2):
            merge = merge + word2[r]
            r += 1
        return merge