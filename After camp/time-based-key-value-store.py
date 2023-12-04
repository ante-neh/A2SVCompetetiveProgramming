class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.timeMap[key]
        
        left, right = -1, len(values)
        while left + 1 < right:
            mid = left + (right - left) // 2

            if timestamp < values[mid][1]:
                right = mid

            else:
                left = mid

        return values[left][0] if left != -1 else ""



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)