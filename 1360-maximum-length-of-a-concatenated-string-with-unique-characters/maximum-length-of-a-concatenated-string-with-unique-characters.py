class Solution:
    def maxLength(self, arr: List[str]) -> int:
        generated = []
        maxLen = 0
        def dfs(cur, start):
            if start > len(arr):
                return

            generated.append("".join(cur[:]))
            for i in range(start, len(arr)):
                dfs(cur + arr[i], i + 1)


        dfs("", 0)


        for gen in generated:
            if len(gen) == len(set(gen)):
                maxLen = max(maxLen, len(gen))


        return maxLen