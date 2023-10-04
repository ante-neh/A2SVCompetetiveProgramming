class Solution:
    def dietPlanPerformance(self, calories, k, lower, upper):
        curSum = 0
        totalPoints = 0
        left = 0

        for right in range(len(calories)):
            curSum += calories[right]

            if right - left + 1 == k:
                if curSum < lower:
                    totalPoints -= 1
                
                elif curSum > upper:
                    totalPoints += 1

                curSum -= calories[left]
                left += 1

        return totalPoints
    
obj = Solution()

print(obj.dietPlanPerformance([1,2,3,4,5], 1, 3, 3))
print(obj.dietPlanPerformance([3,2], 2, 0, 1))
print(obj.dietPlanPerformance([6,5,0,0], 2, 1, 5))