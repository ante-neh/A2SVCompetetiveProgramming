class Solution:
    def mySqrt(self, x: int) -> int:
        low,high=0,x
        while low<=high:
            mid=low+(high-low)//2
            if(mid*mid==x):
                return mid
            elif mid*mid<x:
                low=mid+1
            else:
                high=mid-1
        return (low-1)
            #time complexity O(logn)
            #space complexity O(1)