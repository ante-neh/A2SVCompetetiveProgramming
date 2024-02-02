class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        queue = deque(range(1, 10))
        sequentials = []

        while queue:
            num = queue.popleft()
            if num > high:
                continue

            if low <= num <= high:
                sequentials.append(num)
            
            ones = num % 10
            if ones < 9:
                queue.append(num  * 10  + (ones + 1))

        return sequentials
        
