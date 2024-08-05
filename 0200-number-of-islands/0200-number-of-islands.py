class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return -1
        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r,c))
            directions = [[1,0], [-1,0],[0,1],[0,-1]]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r  = row + dr
                    c = col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visit:
                        q.append((r,c))
                        visit.add((r,c))
                

                
        visit = set()
        rows, cols = len(grid), len(grid[0])
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and grid[r][c] == "1":
                    bfs(r,c)
                    islands+=1

        return islands
        