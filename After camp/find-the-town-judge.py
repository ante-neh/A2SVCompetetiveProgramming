class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incomingToOutgoing = defaultdict(int)

        for start, end in trust:
            incomingToOutgoing[end] += 1
            incomingToOutgoing[start] -= 1

        for i in range(1, n + 1):
            if incomingToOutgoing[i] == n - 1:
                return i

        return -1