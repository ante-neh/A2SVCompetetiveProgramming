class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = []
        result = ['0'] * len(s)

        for c in s:
            if c == "1":
                ones.append(c)
        
        if ones:
            result.insert(0, ones.pop())
            result.pop()

        i = 0
        while ones:
            result[len(s) -i - 1] = ones.pop()
            i += 1
        
        return "".join(result[::-1])