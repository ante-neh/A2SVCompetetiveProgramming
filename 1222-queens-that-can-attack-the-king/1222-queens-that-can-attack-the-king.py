class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queens_pos = set(tuple(position) for position in queens)
        res = []
        
        #finding the top position 
        row, col = king[0], king[1]
        while row >= 0:
            row -= 1
            pos = [row, col]

            if tuple(pos) in queens_pos:
                res.append(list(pos))
                break

        #finding the bottom position

        row, col = king[0], king[1]

        while row < 8:
            row += 1
            pos = [row, col]
            if tuple(pos) in queens_pos:
                res.append(list(pos))
                break

        
        
        #finding the left position 

        row, col = king[0], king[1]

        while col >= 0:
            col -= 1
            pos = [row, col]

            if tuple(pos) in queens_pos:
                res.append(list(pos))
                break

        
        #finding the right position

        row, col = king[0], king[1]

        while col < 8:
            col += 1
            pos = [row, col]

            if tuple(pos) in queens_pos:
                res.append(list(pos))
                break


        
        #finding the top left

        row, col = king[0], king[1]

        while col  >= 0 and row >= 0:
            col -= 1
            row -= 1
            pos = [row, col]

            if tuple(pos) in queens_pos:
                res.append(list(pos))
                break


        
        #finding the bottom right

        row, col = king[0], king[1]

        while col < 8 and row < 8:
            row += 1
            col += 1
            pos= [row, col]

            if tuple(pos) in queens_pos:
                res.append(list(pos))
                break


        
        #finding the top right

        row, col = king[0], king[1]

        while col < 8 and row >= 0:
            row -= 1
            col += 1
            pos= [row, col]

            if tuple(pos) in queens_pos:
                res.append(list(pos))
                break

        
        #finding the bottom left

        row, col = king[0], king[1]

        while col >= 0 and row < 8:
            row += 1
            col -= 1
            pos= [row, col]

            if tuple(pos) in queens_pos:
                res.append(list(pos))
                break
                
        return res