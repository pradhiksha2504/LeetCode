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
                if len(row) == 3:
                    matrix.append(row)
                else:
                    pass
            if magic(matrix,dup):
                count += 1
        def magic(matrix, dup):
            if len(dup)!= 9:
                return False
            d1, d2 = 0, 0
            rowSum, colSum = 0,0
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
                ind += 1
            r, c = 0, 0
            r1,c1 = 2,0
            while r < 3 and c < 3 and r1 >= 0 and c1 <3 :
                d1 += matrix[r][c]
                d2 += matrix[r1][c1]
                r += 1
                c += 1
                r1 -=1
                c1 += 1
            return d1 == d2 == rowSum == colSum

        for i in range(rows):
            for j in range(cols):
                if i+3 <= rows and j+3<=cols:
                    search(i,j)

        return count