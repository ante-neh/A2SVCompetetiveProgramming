class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitsToChar = {'2':'abc', '3':'def','4':'ghi','5':'jkl', '6':'mno', '7':'pqrs','8':'tuv','9':'wxyz'}
        letterCombinations = []
        
        def backtrack(i, cur):
            if len(cur) == len(digits):
                letterCombinations.append(cur[:])
                return 
            
            for c in digitsToChar[digits[i]]:
                backtrack(i + 1, cur + c)
                
        if digits:
            backtrack(0,"")
        
        return letterCombinations