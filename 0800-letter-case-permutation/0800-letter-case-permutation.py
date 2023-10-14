class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []

        def backtrack(currentString, index):
            if index >= len(s):
                result.append(currentString)
                return 

            if s[index].isalpha():
                backtrack(currentString + s[index].upper(), index + 1)
                backtrack(currentString + s[index].lower(), index + 1)
            
            else:
                backtrack(currentString + s[index], index + 1)

        backtrack("", 0)

        return result
            
