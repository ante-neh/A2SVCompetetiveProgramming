class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start,end=0,len(nums)-1
        sortedarray=[]
        while start<=end:
            if abs(nums[start])<abs(nums[end]):
                sortedarray.append(nums[end]**2)
                end-=1
            else:
                sortedarray.append(nums[start]**2)
                start+=1
        return sortedarray[::-1]
    #time complexity O(n) 
    #space complexity O(n)