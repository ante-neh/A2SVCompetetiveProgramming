class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        firstNum = (num - 3) // 3
        threeNums = [firstNum, firstNum + 1, firstNum + 2]
        
        return threeNums if sum(threeNums) == num else []
