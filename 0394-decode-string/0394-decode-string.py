class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        if s.isdigit():
            return ""
        
        for c in s:
            if c != ']': 
                stack.append(c)
            else:
                temp_str, temp_digit = '', ''
                while stack[-1] != '[':
                    temp_str = stack.pop() + temp_str 
                stack.pop() # pop '['
                
                while stack and stack[-1].isdigit(): # avoid pop out index when stack is empty 
                    temp_digit = stack.pop() + temp_digit
                stack.append(int(temp_digit) * temp_str)
        return ''.join(stack)