class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        validIpAddresses = []

        def backtrack(cur, i):
            if i == len(s):
                if len(cur) == 4:
                    validIpAddresses.append(".".join(cur[:]))
                    
                return

            for j in range(i, len(s)):
                sub = s[i:j + 1]
                if self.isValid(sub):
                    cur.append(sub)
                    backtrack(cur, j + 1)
                    cur.pop()

        backtrack([], 0)

        return validIpAddresses

    def isValid(self, s):
        return len(s) == len(str(int(s))) and 0 <= int(s) and int(s) <= 255 

                