class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if rows < 3 or cols < 3:
            return 0
        global count
        count = 0
        
        def search(r, c):
            global count
            matrix = []
            dup = set()
            for i in range(r,r+3):
                row = []
                for j in range(c,c+3):
                    ele = grid[i][j]
                    if ele in range(1,10):
                        row.append(grid[i][j])
                        dup.add(grid[i][j])
                matrix.append(row)
            if magic(matrix,dup):
                count += 1
        def magic(matrix, dup):
            if len(dup)!= 9:
                return False
            d1 = matrix[0][0]+matrix[1][1]+matrix[2][2]
            d2 = matrix[2][0]+matrix[1][1]+matrix[0][2]
            if d1 != d2:
                return False
            rowSum, colSum = 0, 0
            for i in matrix:
                x = sum(i)
                if x == rowSum or rowSum == 0:
                    rowSum = x
                else:
                    return False
            ind = 0
            while ind < 3:
                temp = 0
                for i in range(3):
                    temp += matrix[i][ind]
                if colSum == 0 or temp == colSum:
                    colSum = temp  
                else:
                    return False 
                ind += 1
            
            return d1 == d2 == rowSum == colSum

        for i in range(rows):
            for j in range(cols):
                if i+3 <= rows and j+3<=cols:
                    search(i,j)

        return count