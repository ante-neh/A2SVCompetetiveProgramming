class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        modifiedNum = []
        
        for num in nums:
            if num > 0:
                positive.append(num)
            
            else:
                negative.append(num)
                
        for i in range(len(positive)):
            modifiedNum.append(positive[i])
            modifiedNum.append(negative[i])
            
        return modifiedNum