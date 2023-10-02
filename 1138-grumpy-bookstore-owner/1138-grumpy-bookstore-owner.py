class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        left = 0
        initailCustomers = 0
        maxNumberOfCustomers = 0
        curSum = 0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                initailCustomers += customers[i]
        
        for right in range(len(grumpy)):
            if grumpy[right] == 1:
                curSum += customers[right]

            if right - left + 1 == minutes:
                maxNumberOfCustomers = max(maxNumberOfCustomers, curSum)
                if grumpy[left] == 1:
                    curSum -= customers[left]
                left += 1

        return initailCustomers + maxNumberOfCustomers