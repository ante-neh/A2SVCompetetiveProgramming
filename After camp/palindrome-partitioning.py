class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindromePartitions = []

        def dfs(cur, i):
            if i == len(s):
                palindromePartitions.append(cur[:])
                return

            for j in range(i, len(s)):
                if s[i:j + 1] and s[i:j + 1] == s[i:j + 1][::-1]:
                    cur.append(s[i:j + 1])
                    dfs(cur, j + 1)
                    cur.pop()

        dfs([], 0)

        return palindromePartitions

