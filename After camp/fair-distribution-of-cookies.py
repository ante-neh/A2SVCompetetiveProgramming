class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cur = [0] * k

        def backtrack(i, zeroCount):
            if len(cookies) - i < zeroCount:
                return float("inf")

            if i == len(cookies):
                return max(cur)

            ans = float("inf")

            for j in range(k):
                if cur[j] == 0:
                    zeroCount -= 1
                cur[j] += cookies[i]
                ans = min(ans, backtrack(i + 1, zeroCount))
                cur[j] -= cookies[i]
                if cur[j] == 0:
                    zeroCount += 1

            return ans

        return backtrack(0, k)
