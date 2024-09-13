class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pat = defaultdict(list)
        for i in range(len(pattern)):
            pat[pattern[i]].append(i)
        # print(pat)
        res = []
        
        for word in words:
            if len(set(word)) != len(pat.keys()):
                continue
            temp = defaultdict(list)
            for i in range(len(word)):
                temp[word[i]].append(i)
            for j in temp.values():
                if j not in pat.values():
                    flag = False
                    break
                else:
                    flag = True
            if  flag:
                res.append(word)


            # print(temp)
        return res