class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = list(s)
        shiftingPosition = [0] * (len(s) + 1)

        for start, end, value in shifts:
            if value == 0:
                shiftingPosition[start] -= 1
                shiftingPosition[end + 1] += 1
            else:
                shiftingPosition[start] += 1
                shiftingPosition[end + 1] -= 1

        for i in range(1,len(shiftingPosition)):
            shiftingPosition[i] += shiftingPosition[i - 1]

        for i in range(len(s)):
            order = ord(s[i]) + shiftingPosition[i] % 26
            if order > 122:
                order -= 26
            s[i] = chr(order)

        return "".join(s)
