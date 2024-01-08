class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsFreq = Counter(nums)
        result = []
        def quickSort(nums, k):
            nonlocal result
            pivot = nums[0]
            left, right, mid = [], [], []

            for num in nums:
                if numsFreq[num] > numsFreq[pivot]:
                    left.append(num)
                elif numsFreq[num] < numsFreq[pivot]:
                    right.append(num)
                else:
                    mid.append(num)


            if len(left) == k:
                result.extend(left)
                return left

            elif len(left) > k:
                return quickSort(left, k)

            elif len(left) + len(mid) == k:
                result.extend(left + mid)
                return result

            else:
                result.extend(left + mid)
                return quickSort(right, k - len(left) - len(mid))

        quickSort(list(set(nums)), k)

        return result

