class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        i = 0

        for j in range(1, n + 1):
            stack.append("Push")
            if target[i] == j:
                i += 1
            else:
                stack.append("Pop")

            if i >= len(target):
                break

        return stack