class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToLetter = defaultdict(list)
        letterCombinations = []
        remaining = ["pqrs", "tuv", "wxyz"]
        
        i = 2
        j = 0
        while j < 15:
            for c in range(3 if j != 7 or j != 9 else 4):
                digitToLetter[i].append(chr(ord('a') + j))
                j += 1
            i += 1
        
        i = 7
        for remain in remaining:
            digitToLetter[i].append(remain)
            i += 1
            
        s = []

        for c in digits:
            s.append("".join(digitToLetter[int(c)]))

        def backtrack(cur, index):
            if len(cur) == len(digits):
                letterCombinations.append("".join(cur[:]))
                return

            for i in range(index, len(s)):
                for j in range(len(s[i])):
                    cur.append(s[i][j])
                    backtrack(cur, i + 1)
                    cur.pop()

        for i in range(len(s)):
            backtrack([], i)

        return letterCombinations
