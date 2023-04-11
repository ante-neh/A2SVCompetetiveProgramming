class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        numset=set(range(1,10))
        for rowix in range(1,len(grid)-1):
            row =grid[rowix]
            fiveix = [ix for ix in range(1, len(row)-1) if row[ix] == 5]
            for five in fiveix:
                #five is the col index
                #rowix is the row index of number five
                subgrid = [row[five-1:five+2] for row in grid]
                subgrid = subgrid[rowix-1:rowix+2]
                #check if this subgrid is a magic square

                
                flatgrid=set([item for row in subgrid for item in row])
                diff = numset-flatgrid
                
                row_sum = [1 if sum(row)==15 else 0 for row in subgrid]
                col_sum = [1 if sum(col)==15 else 0 for col in zip(*subgrid)]
                if sum(row_sum) == 3 and sum(col_sum)==3 and len(diff)==0:
                    count +=1
                
                
        return count
                                                     