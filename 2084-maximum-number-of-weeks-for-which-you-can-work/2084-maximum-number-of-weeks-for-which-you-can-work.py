class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        milestones.sort()

        totalSum = sum(milestones)

        if totalSum - milestones[-1] > milestones[-1] - 1:
            return totalSum

        else:
            return (totalSum - milestones[-1]) * 2 + 1