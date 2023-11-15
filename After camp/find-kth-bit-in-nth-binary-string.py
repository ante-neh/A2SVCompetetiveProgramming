class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            newS = ""
            for c in s:
                if c == '1':
                    newS += "0"
                else:
                    newS += '1'

            return newS

        def find(n):
            if n == 1:
                return "0"

            prev = find(n - 1)
            return prev + '1' + invert(prev)[::-1]

        return find(n)[k - 1]