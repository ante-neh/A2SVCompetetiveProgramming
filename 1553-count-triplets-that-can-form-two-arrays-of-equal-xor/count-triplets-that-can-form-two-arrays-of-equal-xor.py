class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        preXor = [arr[0]]
        for i in range(1, len(arr)):
            preXor.append(preXor[i - 1] ^ arr[i])
        
        preXor = [0] + preXor
        count = 0
        for i in range(1, len(preXor)):
            for j in range(i + 1, len(preXor)):
                for k in range(j, len(preXor)):
                    if preXor[j - 1] ^ preXor[i - 1] == preXor[k] ^ preXor[j - 1]:
                        count += 1


        return count 