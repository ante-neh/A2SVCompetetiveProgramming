class Solution:
    def calculate(self, s: str) -> int:
        operator, operand = deque(), deque()
        
        temp_operand = ""
        s = s.replace(' ', '')
        for index ,i in enumerate(s):
            if i.isdigit() and index != len(s) - 1 :
                temp_operand += i
                continue
            else:
                if index == len(s) - 1:
                     temp_operand += i
                if len(operator):
                    prevOperator = operator[-1]
                    if prevOperator == "-":
                        operand.append(-1 * int(temp_operand))
                        operator.pop()
                    elif prevOperator == "*":
                        result = int(temp_operand) * operand.pop()
                        operator.pop()
                        operand.append(result)
                    elif prevOperator == "/":
                        result = int(operand.pop() / int(temp_operand))
                        operator.pop()
                        operand.append(result)
                    else:
                        operand.append(int(temp_operand))
                else:
                    operand.append(int(temp_operand))
                operator.append(i)
                temp_operand = ""
                
        return sum(operand)