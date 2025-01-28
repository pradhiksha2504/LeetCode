class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        for i in words:
            s=i.lower()
            f = {}
            for j in s:
                if j in f:
                    continue
                if j in "qwertyuiop" :
                    f[j]=0
                elif j in "asdfghjkl":
                    f[j]=1
                else:
                    f[j]=2
            if len(set(f.values())) == 1:
                res.append(i)
        return res

                
        