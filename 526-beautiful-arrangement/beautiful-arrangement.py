class Solution:
    def countArrangement(self, n: int) -> int:
        visited = 0
        beautiful = 0

        def backtrack(index):
            nonlocal visited
            nonlocal beautiful
            if index == n + 1:
                beautiful += 1
                return

            for i in range(n):
                if visited & (1 << i) or ((index % (i + 1)) != 0 and ((i + 1) % index) != 0):
                    continue

                visited |= 1 << i
                backtrack(index  + 1)
                visited ^= 1 << i

        backtrack(1)

        return beautiful