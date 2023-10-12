class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefixSum = [0] * 1001

        for passangers, start, end in trips:
            prefixSum[start] += passangers
            prefixSum[end] -= passangers

        for i in range(1, len(prefixSum)):
            prefixSum[i] += prefixSum[i - 1]

        for sum in prefixSum:
            if sum > capacity:
                return False

        return True
        