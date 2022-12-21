class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carryOver = 1
        for i in range(len(digits)-1, -1, -1):
            temp = digits[i] + carryOver
            if temp>9:
                digits[i] = 0
            else:
                digits[i] = temp
                carryOver = 0
                break
        if carryOver == 1 and i == 0:
            digits.insert(0, 1)
        return digits