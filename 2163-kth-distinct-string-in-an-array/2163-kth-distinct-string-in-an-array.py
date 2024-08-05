class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        temp = {}
        for i in arr:
            if i in temp:
                temp[i] += 1
            else:
                temp[i] = 1
        c = 0
        for i, j in temp.items():
            if j == 1:
                c += 1
                if c == k:
                    return i

        return ""
        