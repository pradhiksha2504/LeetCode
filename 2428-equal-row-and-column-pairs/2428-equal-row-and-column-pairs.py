class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        columns = []
        n = len(grid)
        count = 0
        for i in range(n):
            temp = []
            ind = 0
            while ind < n:
                temp.append(grid[ind][i])
                ind += 1
            columns.append(temp)
            # if temp in grid:
                # count += 1
        # count = 0
        print(columns)
        for i in columns:
            count += grid.count(i)
        return count
