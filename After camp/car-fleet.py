class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionSpeedPair = []
        stack = []

        for i in range(len(position)):
            positionSpeedPair.append([position[i], speed[i]])

        positionSpeedPair.sort(key = lambda x : x[0])

        for position, speed in positionSpeedPair:
            time = (target - position) / speed
            while stack and stack[-1] <= time:
                stack.pop()

            stack.append(time)


        return len(stack)
