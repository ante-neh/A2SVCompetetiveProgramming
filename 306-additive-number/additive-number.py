class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def isValid(cur, temp):
            if len(str(int(temp))) != len(temp):
                return False

            if len(cur) < 2:
                return True
            
            return cur[-2] + cur[-1] == int(temp)

        def backtrack(cur, index):
            if index == len(num):
                if len(cur) > 2:
                    return True

            for i in range(index, len(num)):
                temp = num[index: i + 1]
                if isValid(cur, temp):
                    cur.append(int(temp))
                    if backtrack(cur, i + 1):
                        return True

                    cur.pop()

            return False

        return backtrack([], 0)