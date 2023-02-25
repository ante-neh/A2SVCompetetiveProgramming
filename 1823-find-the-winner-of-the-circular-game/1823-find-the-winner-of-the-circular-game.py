class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        #base case: if there is one play left, return the number of the play
        if n == 1:
            return 1
        # recursively call the function with n-1 players and k step size
        # add k-1 to the result to account for the eliminated player
        # use modulo to wrap around to the beginning of the circle
        return (self.findTheWinner(n - 1, k) + k - 1)  % n + 1