#User function Template for python3

class Solution:
    def asteroidCollision(self, N, asteroids):
        # Code here
        stack = []
        
        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                diff = stack[-1] + asteroid
                if diff > 0:
                    asteroid = 0
                
                elif diff < 0:
                    stack.pop()
                    
                else:
                    stack.pop()
                    asteroid = 0
                
                
            if asteroid:
                stack.append(asteroid)
                
                
        return stack


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        asteroids = list(map(int, input().split()))
        ob = Solution()
        res = ob.asteroidCollision(N, asteroids)
        for val in res:
            print(val, end = ' ')
        print()
# } Driver Code Ends