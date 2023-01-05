class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def diagonal(index):
            diag = []
            if index == 0:
                for row in board:
                    diag.append(row[index])
                    index += 1
            else:
                for row in board:
                    diag.append(row[index])
                    index -= 1

            return diag
        
        numX, numO = 0, 0 
        xWins, oWins = False, False
        vertical = []

        for i in range(3):
            for c in board[i]:
                if c == "X":
                    numX += 1
                elif c == "O":
                    numO += 1

            if board[i] == 'XXX':
                xWins = True
            
            elif board[i] == 'OOO':
                oWins = True
            
            vertical.append([row[i] for row in board])

            if vertical[i] == ["X","X","X"]:
                xWins = True
            elif vertical[i] == ["O","O","O"]:
                oWins = True
    
        if diagonal(0) == ["X","X","X"]:
            xWins = True
        elif diagonal(0) == ["O","O","O"]:
            oWins = True
            
        if diagonal(2) == ["X","X","X"]:
            xWins = True
        elif diagonal(2) == ["O","O","O"]:
            oWins = True

        if xWins:
            return not oWins and numX - numO == 1

        elif oWins:
            return numX == numO
        
        else:
            return numX >= numO and numX - numO <= 1
                
            