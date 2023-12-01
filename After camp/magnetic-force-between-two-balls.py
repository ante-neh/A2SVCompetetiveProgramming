class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def isEnough(mid):
            count = 1
            prev = position[0]
            for p in position:
                if p - prev >= mid:
                    count += 1
                    prev = p 

            return count >= m
        
        left, right = 0, position[-1] - position[0] + 1

        while left + 1 < right:
            mid = left + (right - left) // 2
            print(mid)
            if isEnough(mid):
                left = mid

            else:
                right = mid

        return left 