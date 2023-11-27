class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key = lambda num: (abs(x- num), num))
        return sorted(arr[:k])