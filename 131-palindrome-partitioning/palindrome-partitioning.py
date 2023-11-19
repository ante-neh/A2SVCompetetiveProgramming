class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindromePartitions = set()
        def dfs(cur, i):
            if i == len(s):
                palindromePartitions.add(tuple(cur[:]))
                return

            for j in range(i, len(s)):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    cur.append(s[i:j + 1])
                    dfs(cur, j + 1)
                    cur.pop()

        for i in range(len(s)):
            if s[:i + 1] == s[:i + 1][::-1]:
                dfs([], 0)

        return palindromePartitions

