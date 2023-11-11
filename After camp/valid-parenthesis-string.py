class Solution:
    def checkValidString(self, s: str) -> bool:
        def checkValidity(strs, op):
            open, flip =  0, 0

            for i in range(len(strs)):
                if strs[i] == '*':
                    flip += 1
                
                else:
                    open += 1 if strs[i] == op else -1

                if open + flip < 0:
                    return False

            return open <= flip


        return checkValidity(s, '(') and checkValidity(s[::-1], ')')

