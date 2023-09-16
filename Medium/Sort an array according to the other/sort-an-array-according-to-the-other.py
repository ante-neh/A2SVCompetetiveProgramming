#User function Template for python3

class Solution:
    # A1[] : the input array-1
    # N : size of the array A1[]
    # A2[] : the input array-2
    # M : size of the array A2[]
    
    #Function to sort an array according to the other array.
    def relativeSort (self,A1, N, A2, M):
        arrToIndex = {}
        for i in range(M):
            arrToIndex[A2[i]] = i
    
        # Define a custom sorting key function
        def custom_sort_key(item):
            # If the element is in A2, sort by its position in A2
            if item in arrToIndex:
                return (arrToIndex[item], item)
            # If not in A2, sort it to the end using a high index
            else:
                return (float('inf'), item)
    
        # Sort A1 in-place using the custom key function
        A1.sort(key=custom_sort_key)
    
        return A1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int (input ())
    while t > 0:
        n, m = list(map(int, input().split()))
        a1 = list(map(int, input().split()))
        a2 = list(map(int, input().split()))
        
        ob=Solution()
        a1 = ob.relativeSort (a1, n, a2, m)
        print (*a1, end = " ")
        
        print ()
        
        t -= 1

# } Driver Code Ends