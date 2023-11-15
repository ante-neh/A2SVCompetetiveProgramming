class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def find(n, k):
            if n == 1:
                return 0
            
            if k % 2 == 0:
                kth = find(n - 1 , k // 2)

            else:
                kth = find(n - 1, (k + 1) // 2)

            if k % 2 == 0:
                if kth == 0:
                    return 1
                else:
                    return 0

            else:
                return kth

        return find(n, k)