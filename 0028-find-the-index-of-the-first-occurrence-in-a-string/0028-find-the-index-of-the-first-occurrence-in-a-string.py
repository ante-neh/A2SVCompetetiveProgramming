class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        LPS = [0] * len(needle)

        i, j = 0, 1

        while j < len(needle):
            if needle[i] == needle[j]:
                LPS[j] = i + 1
                i += 1
                j += 1

            elif i == 0:
                j += 1
            
            else:
                i = LPS[i - 1]


        needleIndex, sIndex = 0, 0

        while sIndex < len(haystack):
            if needle[needleIndex] == haystack[sIndex]:
                sIndex += 1
                needleIndex += 1

            elif needleIndex == 0:
                sIndex += 1

            else:
                needleIndex = LPS[needleIndex - 1]
            
            if needleIndex == len(needle):
                return sIndex - needleIndex

        return -1



                