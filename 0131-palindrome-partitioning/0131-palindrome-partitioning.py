class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindromePartitions = []
        partition = []        
        def backtrack(idx):
            if idx >= len(s):
                palindromePartitions.append(partition[:])
                return 
            
            for i in range(idx, len(s)):
                if self.isPalindrome(s[idx:i + 1]):
                    partition.append(s[idx:i + 1])
                    backtrack(i + 1)
                    partition.pop()
                
        backtrack(0)
        return palindromePartitions
    
    def isPalindrome(self, subString):
        l, r = 0, len(subString) - 1
        while l < r:
            if subString[l] != subString[r]:
                return False
            l += 1
            r -= 1
            
        return True
            