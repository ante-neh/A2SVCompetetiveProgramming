class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        firstWord = strs[0]

        for i in range(len(firstWord)):
            for word in strs[1:]:
                if i == len(word) or word[i] != firstWord[i]:
                    return prefix

            prefix += firstWord[i]

        return prefix
