class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        state,N = [],len(num)
        
        def backtrack(idx,state):
            if(idx==N):
                if(len(state)>=3):
                    return True
                return False
            
            for i in range(idx+1,N+1):
                temp = num[idx:i]
                if(not state or len(state)==1 or state[-1] + state[-2] == int(temp)):
                    if(len(temp)>=2 and temp.startswith("0")):
                        break
                    state.append(int(temp))
                    if(backtrack(i,state)):
                        return True
                    state.pop()
            return False
        
        return backtrack(0,state)