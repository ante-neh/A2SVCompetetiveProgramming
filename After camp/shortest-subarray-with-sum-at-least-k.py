class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        queue = deque()
        minLength = float("inf")
        prefixSum = 0

        for index, num in enumerate(nums):
            prefixSum += num
            if prefixSum >= k:
                minLength = min(minLength, index + 1)

            while queue and prefixSum - queue[0][0] >= k:
                minLength = min(minLength, index - queue[0][1])
                queue.popleft()

            while queue and queue[-1][0] >= prefixSum:
                queue.pop()

            queue.append([prefixSum, index])

        return minLength if minLength != float("inf") else -1