class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        key = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        res = []
        for i in words:
            flag = True
            s=i.lower()
            if s[0] in "qwertyuiop" :
                ind=0
            elif s[0] in "asdfghjkl":
                ind=1
            else:
                ind=2
            for j in s:
                if j not in key[ind]:
                    flag = False
                    break
            if flag:
                res.append(i)
                
        return res

                
        