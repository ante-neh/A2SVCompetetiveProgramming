#User function Template for python3
from collections import defaultdict

def findIndex(arr,X,Y,N):
    # Your code goes here
    freq = defaultdict(int)
    maxIndex = 0
    
    for i in range(len(arr)):
        if arr[i] == X or arr[i] == Y:
            freq[arr[i]] += 1 
            
        if (freq[X] != 0 and freq[Y] != 0) and freq[X] == freq[Y]:
            maxIndex = i
            
    return -1 if maxIndex == 0 else maxIndex
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    #n=int(input())
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    y=l[2]
    a = list(map(int,input().split()))
    ans=findIndex(a,x,y,n)
    print(ans)

# } Driver Code Ends