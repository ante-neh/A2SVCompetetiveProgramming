class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        left = 0 
        radius = 0

        for house in houses:
            while left + 1 < len(heaters) and abs(heaters[left] - house) >= abs(heaters[left + 1] - house):
                left += 1
            
            radius = max(abs(heaters[left] - house), radius)

        return radius 