class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        combinations = set()

        def backtrack(cur, index):
            if len(cur) == len(s):
                combinations.add("".join(cur[:]))
                return

            for i in range(index, len(s)):
                cur.append(s[i].upper())
                backtrack(cur, i + 1)
                cur.pop()
                cur.append(s[i].lower())
                backtrack(cur, i + 1)
                cur.pop()


        backtrack([], 0)
        
        return combinations