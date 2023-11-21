class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        def isValid(cur, temp):
            if len(temp) > 1 and temp[0] == '0':
                return False
            if int(temp) > 2 ** 31:
                return False
                
            if len(cur) < 2:
                return True

            return cur[-1] + cur[-2] == int(temp)


        def backtrack(cur, index):
            if index == len(num):
                if len(cur) > 2:
                    return cur[:]

            for i in range(index, len(num)):
                temp = num[index:i + 1]
                if isValid(cur, temp):
                    cur.append(int(temp))
                    res = backtrack(cur, i + 1)
                    if res:
                        return res

                    cur.pop()

            return

        return backtrack([], 0)