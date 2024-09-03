class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != (m*n):
            return []
        matrix = []
        ind = 0
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(original[ind])
                ind += 1
            matrix.append(temp)
        return matrix
        