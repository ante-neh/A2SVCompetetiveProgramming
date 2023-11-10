class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        def validate(strs, lock, par):
            balance, flip = 0, 0
            for index, c in enumerate(strs):
                if lock[index] == '1':
                    balance += 1 if c == par else -1

                else:
                    flip += 1

                if flip + balance < 0:
                    return False

            return balance <= flip


        return len(s) % 2 == 0 and (validate(s, locked, '(') and validate(s[::-1], locked[::-1], ')'))

