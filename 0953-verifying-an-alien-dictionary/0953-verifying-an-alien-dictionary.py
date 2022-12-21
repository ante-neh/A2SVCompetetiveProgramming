class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderIndex = {c:i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False

                if words[i][j] != words[i + 1][j]:
                    if orderIndex[words[i][j]] > orderIndex[words[i + 1][j]]:
                        return False
                    break

        return True