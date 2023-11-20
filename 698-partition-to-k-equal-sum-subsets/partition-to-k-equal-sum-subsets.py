class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        subset = [0] * k
        target = sum(nums) // k
        nums.sort(reverse = True)

        def backtrack(index):
            if index == len(nums):
                return max(subset) == min(subset)

            for i in range(k):
                if subset[i] + nums[index] <= target:
                    subset[i] += nums[index]
                    if backtrack(index + 1):
                        return True
                    subset[i] -= nums[index]

                    if subset[i] == 0:
                        break
                #         If subSets[j] = 0, it means this is the first time adding values to that subset.
				#         If the backtrack search fails when adding the values to subSets[j] and subSets[j] remains 0, 
                #         it will also fail for all subSets from subSets[j+1:].
				#         Because we are simply going through the previous recursive tree again for a different j+1
                #         position.
				#         So we can effectively break from the for loop or directly return False.
            return False

        return backtrack(0)
