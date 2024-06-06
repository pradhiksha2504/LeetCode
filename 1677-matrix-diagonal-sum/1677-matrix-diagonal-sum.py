class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        add = 0
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            add += mat[i][i]
        for i in range(m):
            j = m-i-1
            if i != j:
                add += mat[i][j]
        return add