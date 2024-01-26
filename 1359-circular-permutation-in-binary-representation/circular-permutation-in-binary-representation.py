class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        return [start ^ i ^ (i >> 1) for i in range(2 ** n)]