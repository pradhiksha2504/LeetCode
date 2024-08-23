class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        visited = set()
        def dfs(r, c):
            for i in range(cols):
                if (r,i) not in visited and matrix[r][i] != 0:
                    # print("i, r: ",i,r)
                    matrix[r][i] = 0
                    visited.add((r,i))
            for i in range(rows):
                if (i,c) not in visited and matrix[i][c]!=0:
                    # print("i, c: ", i,c)
                    matrix[i][c] = 0
                    visited.add((i,c))
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    # print("visited: ", visited)
                    # print(i, j)
                    if (i,j) not in visited:
                        dfs(i, j)
        # print(visited)
        return matrix