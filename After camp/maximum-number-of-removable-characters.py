class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isEnough(mid):
            p1, p2 = 0, 0
            while p1 < len(s) and p2 < len(p):
                if p1 in removed or s[p1] != p[p2]:
                    p1 += 1
                    continue
                
                p2 += 1
                p1 += 1

            return p2 == len(p)

        left, right = -1, len(removable) + 1

        while left + 1 < right:
            mid = left + (right - left) // 2
            removed = set(removable[:mid])
            if isEnough(mid):
                left = mid

            else:
                right = mid

        return left