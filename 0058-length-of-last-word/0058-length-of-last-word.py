class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        lastWord = ""

        for word in s:
            if word != "":
                lastWord = word

        return len(lastWord)