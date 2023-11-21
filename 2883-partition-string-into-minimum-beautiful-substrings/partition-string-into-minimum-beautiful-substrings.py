class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        count = float('inf')
        def backtrack(cur, index):
            nonlocal count
            if index >= len(s):
                count = min(len(cur[:]), count)
                return
            if s[index] == '0':
                return 
                
            for i in range(index, len(s)):
                num = int(s[index:i + 1], 2)
                if num != 0 and math.isclose(math.log(num, 5), round(math.log(num, 5))):
                    cur.append(s[index:i + 1])
                    backtrack(cur, i  + 1)
                    cur.pop()

            return count

        backtrack([], 0)

        return count if count != float('inf') else -1

        