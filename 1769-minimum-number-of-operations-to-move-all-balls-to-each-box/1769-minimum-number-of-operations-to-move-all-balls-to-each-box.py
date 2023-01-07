class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        onesIndex = []
        
        for index, box in enumerate(boxes):
            if box == '1':
                onesIndex.append(index)
         
        operations = []
        for index, box in enumerate(boxes):
            operation = 0
            
            for oneIndex in onesIndex:
                operation += abs(index - oneIndex)
                
            operations.append(operation)
            
        return operations
            
            