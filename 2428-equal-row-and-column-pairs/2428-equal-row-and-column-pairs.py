class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0
        for i in range(n):
            temp = []
            ind = 0
            while ind < n:
                temp.append(grid[ind][i])
                ind += 1
            count += grid.count(temp)
        return count
