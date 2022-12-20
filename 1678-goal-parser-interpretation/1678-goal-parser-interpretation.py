class Solution:
    def interpret(self, command: str) -> str:
        goalParser = ''
        
        for i in range(len(command) - 1):
            if command[i] == 'G':
                goalParser += "G"
                
            elif command[i] == "(" and command[i + 1] == ")":
                goalParser += "o"
                
            elif command[i] == "(" and command[i + 1] == "a":
                goalParser += "al"
                
        if command[len(command) - 1] == "G":
            goalParser += "G"
            
        return goalParser
            
    