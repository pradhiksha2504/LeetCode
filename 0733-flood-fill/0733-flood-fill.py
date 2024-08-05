class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return image
        visit = set()
        rows, cols = len(image), len(image[0])

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visit.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col+dc
                    if r in range(rows) and c in range(cols) and  image[r][c] == curr and (r, c) not in visit:
                        image[r][c] = color
                        q.append((r, c))
                        visit.add((r,c))
            # return image

        curr = image[sr][sc]
        image[sr][sc] = color
        bfs(sr, sc)
        return image
        