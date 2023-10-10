#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        left = 0
        curSum = 0
        maxSum = float('-inf')
        
        for right in range(N):
            curSum += Arr[right]
            
            if right - left + 1 == K:
                maxSum = max(maxSum, curSum)
                curSum -= Arr[left]
                left += 1
                
        return maxSum
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends