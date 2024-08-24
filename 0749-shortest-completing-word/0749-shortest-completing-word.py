class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = licensePlate.lower()
        # print(licensePlate)
        f = Counter(licensePlate)
        # print(f)
        ans = []
        ind, x = 0, 0
        for i in words:
            count = Counter(i)
            # print(count)
            for k, v in f.items():
                if k.isalpha():
                    ind += 1
                    # print("k: ",k)
                    if k in count:
                        # print("k count: ", k)
                        if count[k] >= v:
                            x += 1
                        else:
                            break
            if ind == x:
                ans.append(i)
            ind, x = 0,0
        # print("ans: ", ans)
        return sorted(ans, key=lambda x:len(x))[0] if len(ans) > 0 else ""
