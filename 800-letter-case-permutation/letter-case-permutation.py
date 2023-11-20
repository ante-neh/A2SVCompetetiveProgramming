class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        combinations = []

        def backtrack(cur, index):
            if index >= len(s):
                combinations.append(cur)
                return 

            if s[index].isalpha():
                backtrack(cur + s[index].lower(), index + 1)
                backtrack(cur + s[index].upper(), index + 1)

            else:
                backtrack(cur + s[index], index + 1)

        backtrack("", 0)

        return combinations