class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        maxPoints = 0
        curSum = 0
        totalPoint = sum(cardPoints)
        if k == len(cardPoints):
            return totalPoint

        for right in range(len(cardPoints)):
            curSum += cardPoints[right]
            if right - left + 1 == len(cardPoints) - k:
                maxPoints = max(maxPoints, totalPoint - curSum)
                curSum -= cardPoints[left]
                left += 1
        
        return maxPoints