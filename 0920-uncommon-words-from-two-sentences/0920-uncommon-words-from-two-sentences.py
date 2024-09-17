class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res = []
        s1, s2 = list(s1.split()), list(s2.split())
        for i in s1+s2:
            if (i in s1 and i not in s2 and s1.count(i) == 1) or (i in s2 and i not in s1 and s2.count(i)==1):
                res.append(i)

        return res
        