from typing import List


class Solution:
    def totalCuts(self, N : int, K : int, A : List[int]) -> int:
        # code here
        count = 0
        leftLargest = []
        rightSmallest = []
        cur = 0
        
        for i in range(len(A)):
            cur = max(cur, A[i])
            leftLargest.append(cur)
            
            
        cur = float("inf")
        
        for i in range(N - 1, -1, -1):
            rightSmallest.append(cur)
            cur = min(cur, A[i])
        
            
        rightSmallest = rightSmallest[::-1]

        for i in range(N - 1):
            if leftLargest[i] + rightSmallest[i] >= K:
                count += 1
                
                
        return count
            



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        K = int(input())
        
        
        A=IntArray().Input(N)
        
        obj = Solution()
        res = obj.totalCuts(N,K,A)
        
        print(res)
        

# } Driver Code Ends