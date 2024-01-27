class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # use the subarray sum equal k approach 
        xorFreq = {0:[0, 1]}
        preXor = 0
        count = 0

        for i in range(len(arr)):
            preXor ^= arr[i]
            if preXor in xorFreq:
                count += (i * xorFreq[preXor][1]) - xorFreq[preXor][0]
                xorFreq[preXor][0] += i + 1
                xorFreq[preXor][1] += 1

            else:
                xorFreq[preXor] = [i +1, 1]

        return count
