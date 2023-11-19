class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToLetter = defaultdict(list)
        letterCombinations = []
        digitToLetter= {
            "2": "abc",
            "3": "def", 
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        s = []

        for c in digits:
            s.append(digitToLetter[c])

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
