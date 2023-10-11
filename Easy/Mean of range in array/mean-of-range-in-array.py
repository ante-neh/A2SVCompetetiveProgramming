#User function Template for python3

class Solution:  
    def findMean(self, arr, queries, n, q): 
        # Complete the function
        prefixSum = [0]
        mean = []
        
        for num in arr:
            prefixSum.append(prefixSum[-1] + num)
            

        for i in range(1, len(queries), 2):
            mean.append((prefixSum[queries[i] + 1] - prefixSum[queries[i - 1]]) // (queries[i] - queries[i - 1] + 1) )
            
        return mean

#{ 
 # Driver Code Starts
#Initial Template for Python 3

    
for _ in range(0,int(input())):
    n,q = map(int,input().strip().split())
    arr = list(map(int,input().strip().split()))
    queries = list(map(int,input().strip().split()))
    ob=Solution()
    v = ob.findMean(arr, queries, n, 2*q)
    print(*v)
    
# } Driver Code Ends