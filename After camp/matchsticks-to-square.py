class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
            
        sides = [0] * 4
        target = sum(matchsticks) // 4
        matchsticks.sort(reverse = True)

        def backtrack(index, remaining):
            if index == len(matchsticks):
                return max(sides) == min(sides)

            for i in range(len(sides)):
                if sides[i] + matchsticks[index] <= target:
                    if sides[i] == 0:
                        remaining -= 1
                    
                    sides[i] += matchsticks[index]

                    if backtrack(index + 1, remaining):
                        return True

                    sides[i] -= matchsticks[index]
                    if sides[i] == 0:
                        remaining += 1

            return False

        return backtrack(0, 4)