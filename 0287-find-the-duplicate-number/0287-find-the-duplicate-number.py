class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i=0
        n=len(nums)
        
        #STEP 1- Cyclic sort list
        while(i<n):
            if(nums[i]!= i+1):
                correct_pos= nums[i]-1
                
                if(nums[i]== nums[correct_pos]):
                    i+=1
                else:
                    nums[i],nums[correct_pos]= nums[correct_pos],nums[i]
            else:
                i+=1
        
        
        #STEP 2 - Finding element != index +1 - That must be the repeated element.
        i=0
        for i in range(0,n):
            if nums[i]!= i+1:
                return nums[i]