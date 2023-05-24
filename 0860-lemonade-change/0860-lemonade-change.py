class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        billsFreq = Counter()
        
        for bill in bills:
            if bill == 5:
                billsFreq[5] += 1 
            
            elif billsFreq[5] > 0 and bill == 10:
                billsFreq[10] += 1
                billsFreq[5] -= 1
            
            elif bill == 20:
                if billsFreq[10] > 0 and billsFreq[5] > 0:
                    billsFreq[10] -= 1
                    billsFreq[5] -= 1
                
                elif billsFreq[5] >= 3:
                    billsFreq[5] -= 3
                
                else:
                    return False
            else:
                return False
            
        return True