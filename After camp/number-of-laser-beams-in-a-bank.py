class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prevDevNum = 0
        numberOfLaser = 0

        for row in bank:
            curDevNum = 0
            for c in row:
                if c == '1':
                    curDevNum += 1

            numberOfLaser += curDevNum * prevDevNum
            if curDevNum:
                prevDevNum = curDevNum

        return numberOfLaser
            
