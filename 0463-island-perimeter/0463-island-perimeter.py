class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            if r >= rows or c >= cols or grid[r][c] == 0 or r < 0 or c < 0:
                return 1
            if (r,c) in visit:
                return 0
            visit.add((r, c))
            perim = dfs(r, c+1)
            perim += dfs(r+1, c)
            perim += dfs(r, c-1)
            perim += dfs(r-1, c)
            return perim
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(i, j)


