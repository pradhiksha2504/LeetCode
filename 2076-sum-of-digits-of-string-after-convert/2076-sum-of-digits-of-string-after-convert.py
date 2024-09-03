class Solution:
    def getLucky(self, s: str, k: int) -> int:
        al = "abcdefghijklmnopqrstuvwxyz"
        a = ""
        for i in s:
            ind = al.index(i)
            a+=str(ind+1)
        res = 0
        for i in range(k):
            res = 0
            for j in a:
                res+=int(j)
            a = str(res)
            
            
        return res