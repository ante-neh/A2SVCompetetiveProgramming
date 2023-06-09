class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low, high = -1, len(letters)
        
        while high > low + 1:
            mid = low + (high - low) // 2
            
            if letters[mid] <= target:
                low = mid
            else:
                high = mid
                
        return letters[high] if high != len(letters) else letters[0]
        
        