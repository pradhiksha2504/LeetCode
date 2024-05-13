class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or  len(s) <= numRows:
            return s
        l = [""] * numRows
        ind = 0
        step = 1
        for i in s:
            l[ind] += i
            if ind == 0:
                step = 1
            elif ind == numRows-1:
                step = -1
            ind += step
        return "".join(l)
