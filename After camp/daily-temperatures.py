class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        numberOfDays = [0] * len(temperatures)
        queue = deque()

        for index, val in enumerate(temperatures):
            while queue and queue[-1][0] < val:
                value, ind = queue.pop()
                numberOfDays[ind] = index - ind

            queue.append([val, index])

        
        return numberOfDays