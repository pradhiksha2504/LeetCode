class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        for i in range(9):
            for j in range(9):
                x = board[i][j]
                if x == ".":
                    continue
                if (x in cols[j] or x in rows[i] or x in squares[(i//3,j//3)]):
                    return False
                cols[j].add(x)
                rows[i].add(x)
                squares[i//3,j//3].add(x)
        return True

        