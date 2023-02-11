class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = 0
        
        for operation in operations:
            if operation[0] == "-":
                count -= 1
            elif operation[0] == "+":
                count += 1
                
            else:
                if operation[1] == "+":
                    count += 1
                else:
                    count -= 1
                    
        return count