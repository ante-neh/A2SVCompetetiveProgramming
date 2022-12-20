class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        mDistanceIndex, minDis = -1, float("inf")
        
        for i,point in enumerate(points):
            if point[0] == x or point[1] == y:
                curDis = abs(x - point[0]) + abs(y - point[1])
                
                if curDis < minDis:
                    mDistanceIndex, minDis = i, curDis
                    
        return mDistanceIndex