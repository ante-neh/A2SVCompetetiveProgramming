class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0]

        for i in range(len(arr)):
            prefix.append(arr[i] ^ prefix[-1])

        result = []

        for start, end in queries:
            result.append(prefix[end + 1] ^ prefix[start])

        return result