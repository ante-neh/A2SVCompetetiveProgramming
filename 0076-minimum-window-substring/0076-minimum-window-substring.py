class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Initialization: 
            # need{elements in t}; 
            # window{needed elements in window}; 
            # valid counts the valid needed elements in window
            # length set larger than the original length, if it does not change in the end, we should return none
        left, right = 0, 0
        need = dict()
        window = dict()
        valid = 0 
        length = float('inf')
        
        for ele in t:
            if ele not in need:
                need.update({ele:1})
            else:
                need[ele] += 1
                
        while right < len(s):
            ele = s[right]
            right += 1
            if ele in need:
                if ele not in window:
                    window.update({ele: 1})
                else:
                    window[ele] += 1
                if window[ele] == need[ele]:
                    valid += 1
                    
            while valid == len(need):
                if right - left < length:
                    length = right - left
                    start, end = left, right
                ele = s[left]
                left += 1
                if ele in need:
                    if window[ele] == need[ele]:
                        valid -= 1
                    window[ele] -= 1
               
                    
        if length == float('inf'):
            return ""
        else:
            return s[start:end]