class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxLen = 0

        for trip in trips:
            maxLen = max(maxLen, trip[-1])

        prefix = [0] * (maxLen + 1)

        for trip in trips:
            prefix[trip[1]] += trip[0]
            prefix[trip[2]] -= trip[0]

        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]

        print(prefix)
        for i in range(len(prefix)):
            if prefix[i] > capacity:
                return False

        return True