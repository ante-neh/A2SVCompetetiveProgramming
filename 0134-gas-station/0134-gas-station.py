class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        a , b = 0 , 0
        for x in gas : a += x
        for x in cost : b += x
        if a < b : return -1

        i , j = 0 , 1
        val = gas[i] - cost[i]
        while j < len(gas) :
            if val < 0 :
                i = j
                val = gas[i] - cost[i]
            else :
                val += gas[j] - cost[j]
            j += 1
        return i


                