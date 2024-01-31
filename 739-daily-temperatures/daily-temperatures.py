class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        waitingDays = [0] * len(temperatures)
        stack = []

        for index, temperature in enumerate(temperatures):
            while stack and stack[-1][0] < temperature:
                val, i = stack.pop()
                waitingDays[i] = index - i

            stack.append([temperature, index])

        return waitingDays