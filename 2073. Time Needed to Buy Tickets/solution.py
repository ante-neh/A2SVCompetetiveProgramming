class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = []
        count = 0
        
        for i, v in enumerate(tickets):
            queue.append([i, v])
            
        while tickets[k] > 0:
            if queue[0][1] != 0:
                count += 1
                queue[0][1] -= 1
                if queue[0][0] == k:
                    tickets[k] -= 1
            queue.append(queue.pop(0))
            
        return count 