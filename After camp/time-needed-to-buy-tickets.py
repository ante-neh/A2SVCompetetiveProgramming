class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = [[val, index] for index, val in enumerate(tickets)]
        timeTaken = 0

        while tickets[k] != 0:
            queue[0][0] -= 1
            timeTaken += 1
            if queue[0][1] == k:
                tickets[k] -= 1

            val, index = queue.pop(0)
            if val:
                queue.append([val, index])

        return timeTaken

