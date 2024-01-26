class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        result = [i ^ (i >> 1) for i in range(2 ** n)]
        i = 0
        while i < len(result):
            if result[i] == start:
                break
            i += 1

        return result[i:] + result[:i]