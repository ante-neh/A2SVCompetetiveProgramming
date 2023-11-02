class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        left = 0
        slidingWindowMaximum = []

        for right in range(len(nums)):
            while queue and queue[-1] < nums[right]:
                queue.pop()

            queue.append(nums[right])

            if right - left + 1 == k:
                slidingWindowMaximum.append(queue[0])
            
                if queue[0] == nums[left]:
                    queue.popleft()
                
                left += 1

        return slidingWindowMaximum