class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        f = {}
        for i in licensePlate:
            if i.isalpha():
                i = i.lower()
                if i in f:
                    f[i] += 1
                else:
                    f[i] = 1
        ans = []
        length = len(f.keys())
        ind = 0
        for i in words:
            count = Counter(i)
            for k, v in f.items():
                if k in count:
                    if count[k] >= v:
                        ind += 1
                        continue
                    else:
                        break
            if ind == length:
                ans.append(i)
            ind = 0
        return sorted(ans, key=lambda x:len(x))[0]
