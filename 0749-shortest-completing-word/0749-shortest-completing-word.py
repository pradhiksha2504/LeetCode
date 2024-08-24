class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = licensePlate.lower()
        f = Counter(licensePlate)
        ans = []
        ind, x = 0, 0
        for i in words:
            count = Counter(i)
            for k, v in f.items():
                if k.isalpha():
                    ind += 1
                    if k in count:
                        if count[k] >= v:
                            x += 1
                        else:
                            break
            if ind == x:
                ans.append(i)
            ind, x = 0,0
        return sorted(ans, key=lambda x:len(x))[0] if len(ans) > 0 else ""
